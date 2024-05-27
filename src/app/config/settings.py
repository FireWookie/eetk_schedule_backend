import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class PostgresDatabaseSettings:
    DATABASE_NAME: str = os.environ.get("POSTGRES_DB")
    HOST: str = os.environ.get("POSTGRES_HOST")
    PORT: str = os.environ.get("POSTGRES_PORT")
    USER: str = os.environ.get("POSTGRES_USER")
    PASSWORD: str = os.environ.get("POSTGRES_PASSWORD")
    DSN: str = (
        f"postgresql+asyncpg://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE_NAME}"
    )
