# test_crud.py
from database import SessionLocal
from models import TransactionType
from crud_operations import UserCRUD, CategoryCRUD, TransactionCRUD


def test_user_crud():
    """Тестування User CRUD"""
    print("=== TEST USER CRUD ===\n")

    session = SessionLocal()

    # CREATE
    print("1️⃣ CREATE — додавання користувача")
    user = UserCRUD.create(session, "ivan_test", "ivan@test.com", "hash123")
    print(f"✅ Користувач створений: ID {user.id}, {user.username}\n")

    # READ
    print("2️⃣ READ — отримання користувача")
    fetched = UserCRUD.get_by_username(session, "ivan_test")
    print(f"✅ Знайдено: {fetched.username} ({fetched.email})\n")

    # UPDATE
    print("3️⃣ UPDATE — оновлення користувача")
    updated = UserCRUD.update(session, user.id, email="ivan.new@test.com")
    print(f"✅ Email оновлений: {updated.email}\n")

    # DELETE
    print("4️⃣ DELETE — видалення користувача")
    deleted = UserCRUD.delete(session, user.id)
    print(f"✅ Користувач видалений: {deleted}\n")

    session.close()


def test_transaction_crud():
    """Тестування Category та Transaction CRUD (для Expense Tracker)"""
    print("=== TEST TRANSACTION CRUD ===\n")

    session = SessionLocal()

    # Створити користувача та категорію для тесту
    user = UserCRUD.create(session, "test_author", "author@test.com", "hash")
    category = CategoryCRUD.create(session, "Food", TransactionType.EXPENSE, user.id)

    # CREATE
    print("1️⃣ CREATE — додавання транзакції")
    tx = TransactionCRUD.create(session, 250.0, TransactionType.EXPENSE, category.id, user.id, "Обід у кафе")
    print(f"✅ Транзакцію створено: ID {tx.id}, {tx.amount} грн ({tx.description})\n")

    # READ
    print("2️⃣ READ — отримання транзакції")
    fetched = TransactionCRUD.get_by_id(session, tx.id)
    print(f"✅ Знайдено: {fetched.description} — {fetched.amount} грн (тип: {fetched.transaction_type.value})\n")

    # UPDATE
    print("3️⃣ UPDATE — оновлення суми та опису")
    updated = TransactionCRUD.update(session, tx.id, amount=320.0, description="Обід та кава")
    print(f"✅ Оновлено: {updated.description} — {updated.amount} грн\n")

    # Очистка тестових даних
    TransactionCRUD.delete(session, tx.id)
    CategoryCRUD.delete(session, category.id)
    UserCRUD.delete(session, user.id)

    session.close()


if __name__ == "__main__":
    test_user_crud()
    test_transaction_crud()
    print("✅ Всі тести пройшли успішно!")
