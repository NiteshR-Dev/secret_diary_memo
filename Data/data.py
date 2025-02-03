"""Data For the app"""
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Users:
    user_id: int | None
    user_name: str | None
    password: str | None
    secret_key: str | None
    created_at: str | datetime | None


@dataclass
class Journel:
    journel_id: int | None
    user_id: int | None
    title: str | None
    description: str | None
    created_at: str | datetime | None
    modified_at: str | datetime | None


@dataclass
class Entry:
    entry_id: int | None
    journel_id: int | None
    title: str | None
    content: str | None
    created_at: str | datetime | None
    modified_at: str | datetime | None
