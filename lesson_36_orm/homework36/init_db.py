# init_db.py
from database import engine, Base, init_db
from models import *

if __name__ == "__main__":
    print("🔄 Ініціалізація БД...")
    init_db()
    print("✅ Таблиці успішно створені!")

    print("\n📊 Створені таблиці:")
    for table_name in Base.metadata.tables.keys():
        print(f"  - {table_name}")
