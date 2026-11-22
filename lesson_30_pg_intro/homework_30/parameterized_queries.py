# parameterized_queries.py
import psycopg

DSN = "postgresql://postgres:11223344@localhost:5432/expense_tracker"

def demonstrate_sql_injection():
    """Показати різницю між небезпечним та безпечним кодом"""
    
    print("=== ПАРАМЕТРИЗОВАНІ ЗАПИТИ ===\n")
    
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            
            # Тестові дані
            print("1️⃣  Вставляємо тестові дані:\n")
            
            cur.execute(
                "INSERT INTO users (username, email) VALUES (%s, %s);",
                ("alice_wonderland", "alice@example.com")
            )
            conn.commit()
            print("✅ Вставлено: alice_wonderland\n")
            
            # Безпечний пошук (параметризований запит)
            print("2️⃣  БЕЗПЕЧНИЙ пошук за username:\n")
            search_username = "alice_wonderland"
            
            cur.execute(
                "SELECT id, username, email FROM users WHERE username = %s;",
                (search_username,)
            )
            result = cur.fetchone()
            if result:
                print(f"✅ Знайдено: {result}\n")
            
            # Небезпечна спроба (мовна ілюстрація — НЕ виконуємо!)
            print("3️⃣  НЕБЕЗПЕЧНИЙ код (для демонстрації):\n")
            print("❌ НІКОЛИ не робіть так:")
            dangerous_username = "admin'; DROP TABLE users; --"
            dangerous_query = f"SELECT * FROM users WHERE username = '{dangerous_username}';"
            print(f"   {dangerous_query}")
            print("   ^ Це видалить всю таблицю користувачів!\n")
            
            # Правильний способ з параметрами
            print("✅ ПРАВИЛЬНО з параметрами:")
            print("   cur.execute(")
            print("       \"SELECT * FROM users WHERE username = %s;\",")
            print(f"       ('{dangerous_username}',)")
            print("   )")
            print("   ^ Шукає користувача з буквальною назвою, тому безпечно\n")
            
            # Приклад з кількома параметрами
            print("4️⃣  Приклад з кількома параметрами:\n")
            
            cur.execute(
                "INSERT INTO users (username, email) VALUES (%s, %s);",
                ("bob_builder", "bob@example.com")
            )
            conn.commit()
            
            # Оновлення з кількома параметрами
            cur.execute(
                "UPDATE users SET email = %s WHERE username = %s;",
                ("bob.new@example.com", "bob_builder")
            )
            conn.commit()
            print("✅ Оновлено: bob_builder → bob.new@example.com\n")
            
            # Видалення з параметром
            cur.execute(
                "DELETE FROM users WHERE username = %s;",
                ("bob_builder",)
            )
            conn.commit()
            print("✅ Видалено: bob_builder\n")

if __name__ == "__main__":
    try:
        demonstrate_sql_injection()
    except psycopg.Error as e:
        print(f"❌ Помилка: {e}")
