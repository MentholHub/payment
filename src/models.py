# from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from decimal import Decimal

from sqlmodel import Field, Relationship, SQLModel


class UserBase(SQLModel):
    balance: Decimal = Field(
        default=Decimal("0.0000"),
        max_digits=19,
        decimal_places=4,
        ge=0)


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    transactions_as_payer: list["Transaction"] = Relationship(
        back_populates="payer", sa_relationship_kwargs={
            "primaryjoin": "User.id == Transaction.payer_id"})
    transactions_as_payee: list["Transaction"] = Relationship(
        back_populates="payee", sa_relationship_kwargs={
            "primaryjoin": "User.id == Transaction.payee_id"})
    freezedfunds_as_mentor: list["FreezedFund"] = Relationship(
        back_populates="mentor", sa_relationship_kwargs={
            "primaryjoin": "User.id == FreezedFund.mentor_id"})
    freezedfunds_as_mentee: list["FreezedFund"] = Relationship(
        back_populates="mentee", sa_relationship_kwargs={
            "primaryjoin": "User.id == FreezedFund.mentee_id"})


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    balance: Decimal | None = None


class TransactionBase(SQLModel):
    payer_id: int = Field(foreign_key="user.id")
    payee_id: int = Field(foreign_key="user.id")
    amount: Decimal = Field(max_digits=19, decimal_places=4, ge=0)
    status: str = Field(max_length=10, index=True)
    type: str = Field(max_length=20, index=True)
    external_transaction_id: int = Field(index=True)
    description: str | None = Field(max_length=255)
    error_message: str | None


class Transaction(TransactionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    payer: User | None = Relationship(
        back_populates="transactions_as_payer",
        sa_relationship_kwargs={
            "foreign_keys": "[Transaction.payer_id]"})
    payee: User | None = Relationship(
        back_populates="transactions_as_payee",
        sa_relationship_kwargs={
            "foreign_keys": "[Transaction.payee_id]"})
    created_at: datetime = Field(
        default_factory=datetime.now,
        nullable=False,
        index=True)
    updated_at: datetime = Field(
        default_factory=datetime.now,
        nullable=False,
        index=True)


class TransactionCreate(TransactionBase):
    payer_id: int
    payee_id: int
    amount: Decimal
    status: str
    type: str
    external_transaction_id: int
    description: str | None
    error_message: str | None


class TransactionUpdate(TransactionBase):
    status: str | None = None
    external_transaction_id: int | None = None
    error_message: str | None = None


class FreezedFundBase(SQLModel):
    mentor_id: int = Field(foreign_key="user.id")
    mentee_id: int = Field(foreign_key="user.id")
    amount: Decimal = Field(max_digits=19, decimal_places=4, ge=0)
    status: str = Field(max_length=10, index=True)


class FreezedFund(FreezedFundBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    mentor: User | None = Relationship(
        back_populates="freezedfunds_as_mentor",
        sa_relationship_kwargs={
            "foreign_keys": "[FreezedFund.mentor_id]"})
    mentee: User | None = Relationship(
        back_populates="freezedfunds_as_mentee",
        sa_relationship_kwargs={
            "foreign_keys": "[FreezedFund.mentee_id]"})
    created_at: datetime = Field(
        default_factory=datetime.now,
        nullable=False,
        index=True)
    updated_at: datetime = Field(
        default_factory=datetime.now,
        nullable=False,
        index=True)


class FreezedFundCreate(FreezedFundBase):
    mentor_id: int
    mentee_id: int
    amount: Decimal
    status: str


class FreezedFundUpdate(FreezedFundBase):
    status: str | None = None
