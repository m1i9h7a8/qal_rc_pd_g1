# crud_operations.py
from sqlalchemy.orm import Session
from models import User, Category, Transaction, TransactionType


# ===== USER CRUD =====

class UserCRUD:
    @staticmethod
    def create(session: Session, username: str, email: str, password_hash: str) -> User:
        """Створити користувача"""
        user = User(username=username, email=email, password_hash=password_hash)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    @staticmethod
    def get_by_id(session: Session, user_id: int) -> User | None:
        """Отримати по ID"""
        return session.query(User).filter(User.id == user_id).first()

    @staticmethod
    def get_by_username(session: Session, username: str) -> User | None:
        """Отримати по username"""
        return session.query(User).filter(User.username == username).first()

    @staticmethod
    def get_all(session: Session, skip: int = 0, limit: int = 10) -> list[User]:
        """Отримати всіх з пагінацією"""
        return session.query(User).offset(skip).limit(limit).all()

    @staticmethod
    def update(session: Session, user_id: int, **kwargs) -> User | None:
        """Оновити користувача"""
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            for key, value in kwargs.items():
                if hasattr(user, key):
                    setattr(user, key, value)
            session.commit()
            session.refresh(user)
        return user

    @staticmethod
    def delete(session: Session, user_id: int) -> bool:
        """Видалити користувача"""
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            session.delete(user)
            session.commit()
            return True
        return False


# ===== CATEGORY CRUD =====

class CategoryCRUD:
    @staticmethod
    def create(session: Session, name: str, cat_type: TransactionType, user_id: int) -> Category:
        """Створити категорію"""
        category = Category(name=name, type=cat_type, user_id=user_id)
        session.add(category)
        session.commit()
        session.refresh(category)
        return category

    @staticmethod
    def get_by_id(session: Session, category_id: int) -> Category | None:
        """Отримати категорію по ID"""
        return session.query(Category).filter(Category.id == category_id).first()

    @staticmethod
    def get_all(session: Session, user_id: int) -> list[Category]:
        """Отримати всі категорії користувача"""
        return session.query(Category).filter(Category.user_id == user_id).all()

    @staticmethod
    def update(session: Session, category_id: int, **kwargs) -> Category | None:
        """Оновити категорію"""
        category = session.query(Category).filter(Category.id == category_id).first()
        if category:
            for key, value in kwargs.items():
                if hasattr(category, key):
                    setattr(category, key, value)
            session.commit()
            session.refresh(category)
        return category

    @staticmethod
    def delete(session: Session, category_id: int) -> bool:
        """Видалити категорію"""
        category = session.query(Category).filter(Category.id == category_id).first()
        if category:
            session.delete(category)
            session.commit()
            return True
        return False


# ===== TRANSACTION CRUD =====

class TransactionCRUD:
    @staticmethod
    def create(
        session: Session,
        amount: float,
        transaction_type: TransactionType,
        category_id: int,
        user_id: int,
        description: str = None,
    ) -> Transaction:
        """Створити транзакцію"""
        transaction = Transaction(
            amount=amount,
            transaction_type=transaction_type,
            category_id=category_id,
            user_id=user_id,
            description=description,
        )
        session.add(transaction)
        session.commit()
        session.refresh(transaction)
        return transaction

    @staticmethod
    def get_by_id(session: Session, transaction_id: int) -> Transaction | None:
        """Отримати транзакцію по ID"""
        return session.query(Transaction).filter(Transaction.id == transaction_id).first()

    @staticmethod
    def get_all(session: Session, skip: int = 0, limit: int = 10) -> list[Transaction]:
        """Отримати всі транзакції"""
        return session.query(Transaction).offset(skip).limit(limit).all()

    @staticmethod
    def update(session: Session, transaction_id: int, **kwargs) -> Transaction | None:
        """Оновити транзакцію"""
        transaction = session.query(Transaction).filter(Transaction.id == transaction_id).first()
        if transaction:
            for key, value in kwargs.items():
                if hasattr(transaction, key):
                    setattr(transaction, key, value)
            session.commit()
            session.refresh(transaction)
        return transaction

    @staticmethod
    def delete(session: Session, transaction_id: int) -> bool:
        """Видалити транзакцію"""
        transaction = session.query(Transaction).filter(Transaction.id == transaction_id).first()
        if transaction:
            session.delete(transaction)
            session.commit()
            return True
        return False
