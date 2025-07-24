from fastapi import Depends, FastAPI, HTTPException
from sqlmodel import Session, select

from src.database import get_session
# from src.models import (FreezedFund, FreezedFundCreate, FreezedFundUpdate,
#                      Transaction, TransactionCreate, TransactionUpdate, User,
#                      UserCreate, UserUpdate)
from src.models import User, UserCreate, UserUpdate

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     init_db()
#     yield

# app = FastAPI(lifespan=lifespan)
app = FastAPI()

# @app.on_event("startup")
# async def startup_event():
#     init_db()


@app.get("/")
def read_root(session: Session = Depends(get_session)):
    return {"ping": "pong!"}


@app.post("/users", response_model=User)
def create_user(
    *,
    user: UserCreate,
        session: Session = Depends(get_session)):
    db_user = User()
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@app.get("/users", response_model=list[User])
def read_users(*, session: Session = Depends(get_session)):
    users = session.exec(select(User)).all()
    return users


@app.get("/users/{id}", response_model=User)
def read_user(*, id: int, session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.id == id)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.patch("/users/{id}", response_model=User)
def update_user(
    *,
    id: int,
    user_update: UserUpdate,
        session: Session = Depends(get_session)):
    db_user = session.exec(select(User).where(User.id == id)).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    user_data = user_update.model_dump(exclude_unset=True)
    for key, value in user_data.items():
        setattr(db_user, key, value)

    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user
