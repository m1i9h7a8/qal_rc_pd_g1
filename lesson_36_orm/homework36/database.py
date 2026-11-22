# database.py
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

# Конфігурація
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:11223344@localhost:5432/expense_tracker_orm"
)

# Створити Engine
engine = create_engine(
    DATABASE_URL,
    echo=False,  # Встановити True для дебагу
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True  # Перевіряти з'єднання перед використанням
)

# Declarative Base
Base = declarative_base()

# SessionLocal для створення сесій
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Функція для отримання сесії (для dependency injection)
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

# Функція для ініціалізації БД
def init_db():
    """Створити всі таблиці"""
    Base.metadata.create_all(bind=engine)
    print("✅ БД ініціалізована")

# Функція для очистки БД (для тестування)
def drop_db():
    """Видалити всі таблиці"""
    Base.metadata.drop_all(bind=engine)
    print("✅ БД очищена")

if __name__ == "__main__":
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version();"))
        print("✅ Підключення до PostgreSQL успішне!")
        print(result.fetchone()[0])
