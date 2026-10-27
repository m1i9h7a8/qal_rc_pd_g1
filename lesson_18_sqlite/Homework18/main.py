from database import init_db
from models import User, Budget, Transaction, InvalidAmountError, InvalidMenuChoiceError, TransactionNotFoundError

class ExpenseTracker(Budget):
    def __init__(self, user):
        super().__init__(user.id)
        self.user = user

    def run(self):
        while True:
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

                    category = input("Введіть категорію (наприклад, Salary/Food): ").strip()
                    description = input("Введіть опис (необов'язково): ").strip()

                    new_t = Transaction(amount, t_type, category, description)
                    self.add_transaction(new_t)
                    print("✅ Успішно збережено в базі даних SQLite!")

                elif choice == "4":
                    print("\n--- Всі транзакції (Дані з SQLite через JOIN) ---")
                    txs = self.list_transactions()
                    if not txs:
                        print("Історія платежів порожня.")
                    else:
                        # Формат виведення згідно з шаблоном домашнього завдання
                        for t in txs:
                            desc_part = f" | {t['description']}" if t['description'] else ""
                            print(f"[{t['id']}] {t['category']} | {t['transaction_type'].upper()} | {t['amount']:.2f} грн{desc_part} | {t['username']}")

                elif choice == "5":
                    print("\n--- Видалення транзакції ---")
                    txs = self.list_transactions()
                    if not txs:
                        print("Нічого видаляти.")
                        continue
                    
                    for t in txs:
                        print(f"ID: {t['id']} | {t['category']}: {t['amount']} грн")
                        
                    try:
                        t_id = int(input("\nВведіть точний ID транзакції для видалення: "))
                        self.delete_transaction(t_id)
                        print("❌ Транзакцію видалено з бази даних.")
                    except ValueError:
                        print("Помилка: Введіть число.")

                elif choice == "6":
                    inc, exp = self.monthly_report()
                    print("\n--- Звіт за поточний місяць ---")
                    print(f"📈 Доходи за місяць: {inc:.2f} грн")
                    print(f"📉 Витрати за місяць: {exp:.2f} грн")

                elif choice == "7":
                    print(f"До побачення, {self.user.username}!")
                    break

            except (InvalidAmountError, TransactionNotFoundError, InvalidMenuChoiceError) as e:
                print(f"⚠️ Помилка: {e}")


if __name__ == "__main__":
    # 1. Спочатку обов'язково створюємо/оновлюємо базу даних
    init_db()
    
    print("--- Вхід у фінансовий менеджер ---")
    name = input("Введіть ваше ім'я: ").strip() or "User"
    email = f"{name.lower()}@example.com"
    
    # 2. Отримуємо або створюємо ID користувача в SQLite
    uid = User.create_user(name, email)
    current_user = User(name, email, uid)
    
    # 3. Запускаємо трекер
    tracker = ExpenseTracker(current_user)
    tracker.run()