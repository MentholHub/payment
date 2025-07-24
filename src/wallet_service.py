import logging

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from .models import Transaction, User, Wallet
from .schemas import CardDetails, DepositRequest, WithdrawRequest

logger = logging.getLogger(__name__)


class WalletService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_user(self, email: str, password: str) -> User:
        user = User(email=email, hashed_password=password)
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def get_user(self, user_id: int) -> User | None:
        result = await self.db.execute(select(User).filter(User.id == user_id))
        return result.scalars().first()

    async def add_card(self, user_id: int, card_details: CardDetails) -> Wallet:
        try:
            user = await self.get_user(user_id)
            if not user:
                raise ValueError("User not found")

            wallet = Wallet(
                user_id=user_id,
                payment_method="card",
                card_last4=card_details.number[-4:],
                card_brand=self._detect_card_brand(card_details.number),
                token_hash="temp_token_hash",
            )

            self.db.add(wallet)
            await self.db.commit()
            await self.db.refresh(wallet)
            return wallet
        except SQLAlchemyError as e:
            logger.error(f"Error adding card: {e}")
            await self.db.rollback()
            raise

    async def get_wallet(self, wallet_id: int) -> Wallet | None:
        result = await self.db.execute(
            select(Wallet).filter(Wallet.id == wallet_id)
        )
        return result.scalars().first()

    async def deposit(self, wallet_id: int, request: DepositRequest) -> Wallet:
        try:
            wallet = await self.get_wallet(wallet_id)
            if not wallet:
                raise ValueError("Wallet not found")

            # Имитация платежной интеграции
            wallet.balance += request.amount

            transaction = Transaction(
                wallet_id=wallet_id,
                amount=request.amount,
                type="deposit",
                status="completed",
                reference="SIMULATED_REF",
            )

            self.db.add(transaction)
            await self.db.commit()
            await self.db.refresh(wallet)
            return wallet
        except SQLAlchemyError as e:
            logger.error(f"Deposit error: {e}")
            await self.db.rollback()
            raise

    async def withdraw(
        self, wallet_id: int, request: WithdrawRequest
    ) -> Wallet:
        try:
            wallet = await self.get_wallet(wallet_id)
            if not wallet:
                raise ValueError("Wallet not found")

            if wallet.balance < request.amount:
                raise ValueError("Insufficient funds")

            # Имитация вывода средств
            wallet.balance -= request.amount

            transaction = Transaction(
                wallet_id=wallet_id,
                amount=request.amount,
                type="withdrawal",
                status="completed",
                reference="SIMULATED_REF",
            )

            self.db.add(transaction)
            await self.db.commit()
            await self.db.refresh(wallet)
            return wallet
        except SQLAlchemyError as e:
            logger.error(f"Withdrawal error: {e}")
            await self.db.rollback()
            raise

    def _detect_card_brand(self, number: str) -> str:
        if number.startswith("4"):
            return "Visa"
        if number.startswith(("5", "2")):
            return "Mastercard"
        if number.startswith("3"):
            return "American Express"
        return "Unknown"
