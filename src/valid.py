from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, PositiveFloat, constr


# Схемы для валидации
class CardDetails(BaseModel):
    number: constr(strip_whitespace=True, min_length=13, max_length=19)
    expiry_month: constr(strip_whitespace=True, min_length=2, max_length=2)
    expiry_year: constr(strip_whitespace=True, min_length=4, max_length=4)
    cvv: constr(strip_whitespace=True, min_length=3, max_length=4)
    owner: str


class WalletCreate(BaseModel):
    user_id: int = Field(..., gt=0)
    card_details: CardDetails


class DepositRequest(BaseModel):
    amount: PositiveFloat


class WithdrawRequest(BaseModel):
    amount: PositiveFloat
    destination: str  # Можно добавить валидацию для криптоадресов


class WalletResponse(BaseModel):
    id: int
    user_id: int
    balance: float
    card_last4: str
    card_brand: str
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True


class TransactionResponse(BaseModel):
    id: int
    wallet_id: int
    amount: float
    type: str
    status: str
    reference: str
    created_at: datetime

    class Config:
        orm_mode = True
