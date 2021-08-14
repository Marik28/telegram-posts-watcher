from typing import Optional

import sqlalchemy.orm
from aiogram.types import User

from .. import tables
from ..exceptions import AlreadySubscribedError


class UsersService:
    def __init__(self, session: sqlalchemy.orm.Session):
        self.session = session

    def _get(self, user_id: int) -> Optional[tables.User]:
        user = (
            self.session
                .query(tables.User)
                .filter(tables.User.id == user_id)
                .first()
        )
        return user

    def user_is_subscribed(self, user: User) -> bool:
        return self._get(user.id) is not None

    def add_user(self, user: User) -> None:
        """
        Добавляет пользователя в БД

        :raises AlreadySubscribedError
        """
        if self.user_is_subscribed(user):
            raise AlreadySubscribedError("Вы уже подписаны на рассылку")
        new_user = tables.User(id=user.id, username=user.username)
        self.session.add(new_user)
        self.session.commit()

    def get_users(self) -> list[tables.User]:
        users = (
            self.session.query(tables.User)
                .all()
        )
        return users

    def delete_user(self, user) -> None:
        user_to_delete = self._get(user.id)

        if user_to_delete is not None:
            self.session.delete(user_to_delete)
            self.session.commit()
