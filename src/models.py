from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Numeric, String
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .db import Base


class User(AsyncAttrs, Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )

    wallets: Mapped[list["Wallet"]] = relationship(
        back_populates="user", lazy="selectin"
    )


class Wallet(AsyncAttrs, Base):
    __tablename__ = "wallets"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    balance: Mapped[float] = mapped_column(Numeric(10, 2), default=0.00)
    token_hash: Mapped[str | None] = mapped_column(String(255))
    card_last4: Mapped[str | None] = mapped_column(String(4))
    card_brand: Mapped[str | None] = mapped_column(String(20))
    crypto_address: Mapped[str | None] = mapped_column(String(255))
    payment_method: Mapped[str] = mapped_column(String(10))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )

    user: Mapped["User"] = relationship(
        back_populates="wallets", lazy="selectin"
    )
    transactions: Mapped[list["Transaction"]] = relationship(
        back_populates="wallet", lazy="selectin"
    )


class Transaction(AsyncAttrs, Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    wallet_id: Mapped[int] = mapped_column(ForeignKey("wallets.id"))
    amount: Mapped[float] = mapped_column(Numeric(10, 2))
    type: Mapped[str] = mapped_column(String(20))
    status: Mapped[str] = mapped_column(String(20), default="pending")
    reference: Mapped[str | None] = mapped_column(String(50))
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )

    wallet: Mapped["Wallet"] = relationship(
        back_populates="transactions", lazy="selectin"
    )
