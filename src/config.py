from os import getenv

POSTGRES_USER: str = getenv("POSTGRES_USER", "USERNAME")
POSTGRES_PASSWORD: str = getenv("POSTGRES_PASSWORD", "PASSWORD")
POSTGRES_DB: str = getenv("POSTGRES_DB", "DATABASE")
WEB_PORT: str = getenv("WEB_PORT", "PORT")

DATABASE_URL: str = getenv("DATABASE_URL", "URL")
DEBUG: bool = getenv(
    "DEBUG",
    "False").lower() in (
        "true",
        "1",
        "yes",
        "t",
    "y")
