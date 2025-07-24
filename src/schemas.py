from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, PositiveFloat, constr


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


class CardDetails(BaseModel):
    number: constr(strip_whitespace=True, min_length=13, max_length=19)
    expiry_month: constr(strip_whitespace=True, min_length=2, max_length=2)
    expiry_year: constr(strip_whitespace=True, min_length=4, max_length=4)
    cvv: constr(strip_whitespace=True, min_length=3, max_length=4)
    owner: str


class WalletCreate(BaseModel):
    card_details: CardDetails


class WalletResponse(BaseModel):
    id: int
    user_id: int
    balance: float
    card_last4: Optional[str] = None
    card_brand: Optional[str] = None
    payment_method: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


class DepositRequest(BaseModel):
    amount: PositiveFloat


class WithdrawRequest(BaseModel):
    amount: PositiveFloat
    destination: Optional[str] = None


class TransactionResponse(BaseModel):
    id: int
    wallet_id: int
    amount: float
    type: str
    status: str
    reference: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True
