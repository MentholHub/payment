from sqlmodel import Session, SQLModel, create_engine

from src.config import DATABASE_URL, DEBUG

engine = create_engine(DATABASE_URL, echo=DEBUG)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
