from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from .db import get_db
from .models import User
from .schemas import (
    DepositRequest,
    UserCreate,
    WalletCreate,
    WithdrawRequest,
)
from .wallet_service import WalletService

router = APIRouter()


@router.post(
    "/users", status_code=status.HTTP_201_CREATED, response_model=UserCreate
)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    service = WalletService(db)
    try:
        return await service.create_user(user.email, user.password)
    except Exception as e:
        raise HTTPException(400, detail=str(e))


@router.post(
    "/users/{user_id}/wallets",
    status_code=status.HTTP_201_CREATED,
    response_model=WalletCreate,
)
async def add_wallet(
    user_id: int, wallet: WalletCreate, db: AsyncSession = Depends(get_db)
):
    service = WalletService(db)
    try:
        return await service.add_card(user_id, wallet.card_details)
    except ValueError as e:
        raise HTTPException(404, detail=str(e))
    except Exception as e:
        raise HTTPException(400, detail=str(e))


@router.post("/wallets/{wallet_id}/deposit", response_model=WalletCreate)
async def deposit(
    wallet_id: int, request: DepositRequest, db: AsyncSession = Depends(get_db)
):
    service = WalletService(db)
    try:
        return await service.deposit(wallet_id, request)
    except ValueError as e:
        raise HTTPException(404, detail=str(e))
    except Exception as e:
        raise HTTPException(400, detail=str(e))


@router.post("/wallets/{wallet_id}/withdraw", response_model=WalletCreate)
async def withdraw(
    wallet_id: int, request: WithdrawRequest, db: AsyncSession = Depends(get_db)
):
    service = WalletService(db)
    try:
        return await service.withdraw(wallet_id, request)
    except ValueError as e:
        if "not found" in str(e):
            raise HTTPException(404, detail=str(e))
        else:
            raise HTTPException(400, detail=str(e))
    except Exception as e:
        raise HTTPException(500, detail="Internal server error")
