# db_connection.py
import psycopg

# Параметри підключення
DSN = "postgresql://postgres:11223344@localhost:5432/lesson_30_test"

try:
    # Підключитися до БД
    with psycopg.connect(DSN) as conn:
        print("✅ Успішно підключені до PostgreSQL!")
        
        # Отримати інформацію про БД
        with conn.cursor() as cur:
            cur.execute("SELECT version();")
            version = cur.fetchone()[0]
            print(f"\n📊 PostgreSQL версія:\n{version}\n")
            
            # Отримати інформацію про поточної користувача
            cur.execute("SELECT current_user;")
            user = cur.fetchone()[0]
            print(f"👤 Користувач: {user}")
            
            # Отримати поточну БД
            cur.execute("SELECT current_database();")
            database = cur.fetchone()[0]
            print(f"📁 Поточна БД: {database}")

except psycopg.Error as e:
    print(f"❌ Помилка підключення: {e}")