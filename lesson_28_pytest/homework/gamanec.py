
from datetime import datetime 
# ==========================================
# 1. НАШІ ВИНЯТКИ (EXCEPTIONS)
# ==========================================
class InvalidAmountError(Exception):
    pass

class TransactionNotFoundError(Exception):
    pass

class InvalidMenuChoiceError(Exception):
    pass


# ==========================================
# 2. КЛАСИ (MODELS)
# ==========================================
class User:
    def __init__(self, username):
        self.username = username


class Transaction:
    def __init__(self, amount, transaction_type, category, description=""):
        if amount <= 0:
            raise InvalidAmountError("Сума повинна бути більшою за 0!")
            
        self.amount = amount
        self.transaction_type = transaction_type  # 'income' або 'expense'
        self.category = category
        self.date = datetime.now()
        self.description = description


# ==========================================
# 3. БІЗНЕС-ЛОГІКА ТА УСПАДКУВАННЯ
# ==========================================
class Budget:
    def __init__(self):
        self.transactions = []  # тут зберігаємо об'єкти класу Transaction

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def delete_transaction(self, index):
        if index < 0 or index >= len(self.transactions):
            raise TransactionNotFoundError("Транзакцію з таким номером не знайдено.")
        return self.transactions.pop(index)

    def list_transactions(self):
        return self.transactions

    def calculate_balance(self):
        balance = 0.0
        for t in self.transactions:
            if t.transaction_type == "income":
                balance += t.amount
            elif t.transaction_type == "expense":
                balance -= t.amount
        return balance

    def monthly_report(self):
        # Рахуємо суми за поточний місяць
        current_month = datetime.now().strftime("%Y-%m")
        income_total = 0.0
        expense_total = 0.0

        for t in self.transactions:
            if t.date.strftime("%Y-%m") == current_month:
                if t.transaction_type == "income":
                    income_total += t.amount
                elif t.transaction_type == "expense":
                    expense_total += t.amount
                    
        return income_total, expense_total


class ExpenseTracker(Budget):
    def __init__(self, user):
        super().__init__()  # ініціалізуємо базовий клас Budget
        self.user = user

    def run(self):
        while True:
            # 1 ПУНКТ — ПОТОЧНИЙ БАЛАНС
            balance = self.calculate_balance()
            print(f"\n=== МЕНЕДЖЕР: {self.user.username.upper()} ===")
            print(f"💰 1. ПОТОЧНИЙ БАЛАНС: {balance:.2f} грн")
            print("2. Додати дохід")
            print("3. Додати витрату")
            print("4. Показати всі транзакції")
            print("5. Видалити транзакцію")
            print("6. Місячний звіт")
            print("7. Вихід")

            try:
                choice = input("\nОберіть дію (1-7): ").strip()
                
                if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
                    raise InvalidMenuChoiceError("Невірний вибір! Введіть число від 1 до 7.")

                if choice == "1":
                    print(f"\n💵 Ваш баланс: {balance:.2f} грн")

                elif choice == "2" or choice == "3":
                    t_type = "income" if choice == "2" else "expense"
                    
                    try:
                        amount = float(input("Введіть суму: ").replace(",", "."))
                    except ValueError:
                        raise InvalidAmountError("Сума повинна бути числом!")

                    category = input("Введіть категорію (наприклад, Salary/Food): ")
                    description = input("Введіть опис (необов'язково): ")

                    # Створюємо об'єкт транзакції та додаємо його
                    new_t = Transaction(amount, t_type, category, description)
                    self.add_transaction(new_t)
                    print("✅ Успішно додано!")

                elif choice == "4":
                    print("\n--- Всі транзакції ---")
                    if not self.transactions:
                        print("Список порожній.")
                    else:
                        for i, t in enumerate(self.transactions, 1):
                            print(f"{i}. [{t.transaction_type.upper()}] {t.category}: {t.amount} грн ({t.description})")

                elif choice == "5":
                    print("\n--- Видалення транзакції ---")
                    if not self.transactions:
                        print("Список порожній.")
                        continue
                        
                    for i, t in enumerate(self.transactions, 1):
                        print(f"{i}. [{t.transaction_type.upper()}] {t.category}: {t.amount} грн")
                        
                    try:
                        num = int(input("\nВведіть номер для видалення: "))
                        self.delete_transaction(num - 1)
                        print("❌ Транзакцію видалено.")
                    except ValueError:
                        print("Помилка: Введіть число.")

                elif choice == "6":
                    inc, exp = self.monthly_report()
                    print("\n--- Звіт за поточний місяць ---")
                    print(f"📈 Доходи: {inc:.2f} грн")
                    print(f"📉 Витрати: {exp:.2f} грн")

                elif choice == "7":
                    print("До побачення!")
                    break

            except (InvalidAmountError, TransactionNotFoundError, InvalidMenuChoiceError) as e:
                print(f"⚠️ Помилка: {e}")


# ==========================================
# ЗАПУСК ПРОГРАМИ
# ==========================================
if __name__ == "__main__":
    name = input("Введіть ваше ім'я: ").strip() or "User"
    user = User(name)
    tracker = ExpenseTracker(user)
    tracker.run()