"""Unility Functions to map tuples response from Sqlite3 to dataclasses"""
from typing import Tuple, List
from Data import Users


def map_user_tuple_to_data(raw_data: list[tuple]) -> List[tuple[Users, list]]:
    """Mapper to mapp user to raw data"""
    users = []
    for user_data in raw_data:
        user_id, user_name, password, secret_key, created_at, *others = user_data
        users.append(
            (Users(
                user_id=user_id,
                user_name=user_name,
                password=password,
                secret_key=secret_key,
                created_at=created_at
            ), others)
        )
    return users
