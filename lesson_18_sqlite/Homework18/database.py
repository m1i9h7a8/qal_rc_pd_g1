import sqlite3
from pathlib import Path

DB_PATH = Path("data/finance.db")

def get_connection():
    """Встановлює з'єднання з базою даних згідно з вимогами."""
    # Автоматично створюємо папку data/, якщо її немає
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH)
    # Налаштування row_factory для доступу за іменами колонок
    conn.row_factory = sqlite3.Row
    # Увімкнення підтримки зовнішніх ключів
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def init_db():
    """Створює таблиці в базі даних, якщо вони не існують."""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Таблиця користувачів
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT UNIQUE
        )
    """)
    
    # Таблиця транзакцій (модель Transaction)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            transaction_type TEXT NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            description TEXT,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )
    """)
    
    conn.commit()
    conn.close()