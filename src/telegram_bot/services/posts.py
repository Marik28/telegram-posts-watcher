import sqlalchemy.orm

from .. import models
from .. import tables


class PostsService:
    def __init__(self, session: sqlalchemy.orm.Session):
        self.session = session

    def get_posts(self, limit: int = 100) -> list[tables.WallPost]:
        posts = (
            self.session.query(tables.WallPost)
                .order_by(tables.WallPost.date.desc())
                .limit(limit)
                .all()
        )
        return posts

    def add_posts(self, posts: list[models.WallPost]) -> None:
        posts_to_add = [tables.WallPost(id=post.id, text=post.text, date=post.date) for post in posts]
        self.session.add_all(posts_to_add)
        self.session.commit()

    def filter_new_posts(self, posts: list[models.WallPost]) -> list[models.WallPost]:
        existing_posts = self.get_posts()
        existing_post_ids = {post.id for post in existing_posts}
        new_posts = [post for post in posts if post.id not in existing_post_ids]
        return new_posts
