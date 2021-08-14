import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class AttachmentType(str, Enum):
    PHOTO = "photo"
    POSTED_PHOTO = "posted_photo"
    VIDEO = "video"
    AUDIO = "audio"
    DOC = "doc"
    GRAFFITI = "graffiti"
    LINK = "link"
    NOTE = "note"
    APP = "app"
    POLL = "poll"
    PAGE = "page"
    ALBUM = "album"
    PHOTOS_LIST = "photos_list"
    MARKET = "market"
    MARKET_ALBUM = "market_album"
    STICKER = "sticker"
    PRETTY_CARDS = "pretty_cards"
    EVENT = "event"


class SizeType(str, Enum):
    S = "s"
    M = "m"
    X = "x"
    O = "o"
    P = "p"
    Q = "q"
    R = "r"
    Y = "y"
    Z = "z"
    W = "w"


class PhotoSize(BaseModel):
    type: SizeType
    url: str
    width: int
    height: int


class Photo(BaseModel):
    id: int
    album_id: int
    owner_id: int
    user_id: Optional[int]
    text: str
    date: datetime.datetime
    sizes: list[PhotoSize]
    width: Optional[int]
    height: Optional[int]


class Video(BaseModel):
    id: int
    owner_id: int
    title: str
    description: str
    duration: int
    date: datetime.datetime
    views: int
    width: int
    height: int


class Attachment(BaseModel):
    type: AttachmentType
    photo: Optional[Photo]
    video: Optional[Video]


class WallPost(BaseModel):
    id: int
    owner_id: int
    is_pinned: Optional[bool]
    from_id: int
    date: datetime.datetime
    text: str
    attachments: Optional[list[Attachment]]
