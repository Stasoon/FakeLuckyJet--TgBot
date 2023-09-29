import os
from typing import Final
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


CODE_WORD = 'BOTJET11'


class Config:
    TOKEN: Final = os.getenv('BOT_TOKEN', 'Впишите токен в .env!')
    __BOT_USERNAME = 'bot_username'

    @classmethod
    def set_bot_username(cls, username: str) -> None:
        cls.__BOT_USERNAME = username

    @classmethod
    def get_bot_username(cls) -> str:
        return cls.__BOT_USERNAME

    DEBUG: Final = bool(os.getenv('DEBUG'))
