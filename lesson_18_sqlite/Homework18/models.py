from datetime import datetime
from database import get_connection

# ВЛАСНІ ВИНЯТКИ
class FinancialTrackerException(Exception): pass
class InvalidAmountError(FinancialTrackerException): pass
class TransactionNotFoundError(FinancialTrackerException): pass
class InvalidMenuChoiceError(FinancialTrackerException): pass


class User:
    def __init__(self, username, email=None, user_id=None):
        self.id = user_id
        self.username = username
        self.email = email

    @staticmethod
    def create_user(username, email=None):
        """Додає користувача в БД та повертає його ID"""
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO users (username, email) VALUES (?, ?)", 
                (username, email)
            )
            conn.commit()
            return cursor.lastrowid
        except Exception:
            # Якщо користувач вже є, просто повертаємо його ID
            cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
            row = cursor.fetchone()
            return row['id'] if row else None
        finally:
            conn.close()


class Transaction:
    def __init__(self, amount, transaction_type, category, description="", date=None, t_id=None):
        if amount <= 0:
            raise InvalidAmountError("Сума повинна бути більшою за 0!")
        self.id = t_id
        self.amount = amount
        self.transaction_type = transaction_type  # 'income' або 'expense'
        self.category = category
        self.date = date or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.description = description


class Budget:
    def __init__(self, user_id):
        self.user_id = user_id

    def add_transaction(self, t: Transaction):
        """Зберігає транзакцію в базі даних SQLite"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO transactions (amount, transaction_type, category, date, description, user_id)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (t.amount, t.transaction_type, t.category, t.date, t.description, self.user_id))
        conn.commit()
        conn.close()

    def delete_transaction(self, t_id):
        """Видаляє транзакцію за її ID в базі даних"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM transactions WHERE id = ? AND user_id = ?", (t_id, self.user_id))
        rows_affected = cursor.rowcount
        conn.commit()
        conn.close()
        if rows_affected == 0:
            raise TransactionNotFoundError("Транзакцію з таким ID не знайдено.")
        return True

    def list_transactions(self):
        """Отримує всі транзакції поточного користувача за допомогою JOIN (імені автора)"""
        conn = get_connection()
        cursor = conn.cursor()
        # Використовуємо JOIN, як вимагає ДЗ
        cursor.execute("""
            SELECT t.id, t.amount, t.transaction_type, t.category, t.date, t.description, u.username
            FROM transactions t
            JOIN users u ON t.user_id = u.id
            WHERE t.user_id = ?
            ORDER BY t.date DESC
        """, (self.user_id,))
        rows = cursor.fetchall()
        conn.close()
        return rows

    def calculate_balance(self):
        """Рахує баланс на основі даних з SQLite"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT 
                SUM(CASE WHEN transaction_type = 'income' THEN amount ELSE 0 END) -
                SUM(CASE WHEN transaction_type = 'expense' THEN amount ELSE 0 END) as balance
            FROM transactions WHERE user_id = ?
        """, (self.user_id,))
        row = cursor.fetchone()
        conn.close()
        return row['balance'] if row['balance'] is not None else 0.0

    def monthly_report(self):
        """Отримує фінансовий звіт за поточний місяць з SQLite"""
        current_month = datetime.now().strftime("%Y-%m")
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT transaction_type, SUM(amount) as total
            FROM transactions
            WHERE user_id = ? AND strftime('%Y-%m', date) = ?
            GROUP BY transaction_type
        """, (self.user_id, current_month))
        
        rows = cursor.fetchall()
        conn.close()
        
        income = 0.0
        expense = 0.0
        for row in rows:
            if row['transaction_type'] == 'income':
                income = row['total']
            elif row['transaction_type'] == 'expense':
                expense = row['total']
                
        return income, expense