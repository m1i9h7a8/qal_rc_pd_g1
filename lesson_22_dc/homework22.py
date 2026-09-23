passwords = [
    "Cossack1",
    "sich",
    "ZAPORIZHZHIA2024",
    "Sich Gate 5",
    "Mazepa99",
    "короткий1",
    "BohunTheBrave",
    "D0br0nich!",
    "аааааааА1",
    "Valid1Pass",
]


def is_strong(password):
    # 1. Перевіряємо довжину від 8 до 20 символів
    if not (8 <= len(password) <= 20):
        return False

    # 2. Перевіряємо відсутність пробілів
    if " " in password:
        return False

    # 3. Перевіряємо наявність хоча б однієї цифри
    has_digit = any(char.isdigit() for char in password)

    # 4. Перевіряємо наявність хоча б однієї великої літери (працює і для укр/англ)
    has_upper = any(char.isupper() for char in password)

    # Пароль надійний, лише якщо є і цифра, і велика літера
    return has_digit and has_upper


# --- Фільтрація за допомогою filter та lambda ---

# 1. Відбираємо надійні паролі (де функція повертає True)
strong_passwords = list(filter(lambda p: is_strong(p), passwords))

# 2. Відбираємо ненадійні паролі (де функція повертає False, тому пишемо not)
weak_passwords = list(filter(lambda p: not is_strong(p), passwords))


# --- Виведення результатів ---

print("--- НАДІЙНІ ПАРОЛІ ---")
for p in strong_passwords:
    print(f"✅ {p} — надійний")

print("\n--- НЕНАДІЙНІ ПАРОЛІ ---")
for p in weak_passwords:
    print(f"❌ {p} — відхилено")



from functools import reduce

raw_registry = [
    "  іван сірко  | полковник | 150",
    "БОГДАН ХМЕЛЬНИЦЬКИЙ | гетьман | 10000",
    "петро дорошенко|сотник|75",
    "  Іван Мазепа | гетьман | 30000 ",
    "семен палій  |  полковник  | 500",
    "  Григорій Сковорода | філософ | 0",
]


# Функція для очищення рядка та перетворення його на словник
def parse_line(line):
    # Розбиваємо рядок по символу "|" і прибираємо зайві пробіли по краях (.strip())
    parts = [part.strip() for part in line.split("|")]

    return {
        "name": parts[0].title(),  # Робимо кожне слово імені з великої літери
        "rank": parts[1].capitalize(),  # Робимо посаду з великої літери
        "warriors": int(parts[2]),  # Перетворюємо кількість воїнів на ціле число
    }


# 1. Застосовуємо map для очищення та створення списку словників
parsed_registry = list(map(parse_line, raw_registry))

# 2. Застосовуємо filter, щоб залишити лише тих, у кого воїнів більше 0
active_registry = list(filter(lambda x: x["warriors"] > 0, parsed_registry))

# 3. Застосовуємо reduce для підрахунку загальної кількості воїнів
# Початкове значення (initializer) дорівнює 0, до нього додаємо воїнів кожного козака
total_warriors = reduce(lambda acc, x: acc + x["warriors"], active_registry, 0)

# 4. Сортуємо за кількістю воїнів від більшого до меншого (reverse=True)
sorted_registry = sorted(
    active_registry, key=lambda x: x["warriors"], reverse=True
)

# --- Виведення красивої таблиці ---

print(f"Козацький реєстр ({len(sorted_registry)} записи):")
print("──────────────────────────────────────────────────────")
print(" №   Ім'я                    Посада        Воїни")
print("──────────────────────────────────────────────────────")

# Перебираємо відсортований реєстр і вирівнюємо текст за допомогою f-рядків
for i, cossack in enumerate(sorted_registry, 1):
    print(
        f" {i:<2} {cossack['name']:<23} {cossack['rank']:<13} {cossack['warriors']}"
    )

print("──────────────────────────────────────────────────────")
print(f"Разом воїнів: {total_warriors}")





messages = [
    "А роза упала на лапу азора",
    "Козак",
    "Зараз",
    "level",
    "Python",
    "А баба",
    "racecar",
    "Запоріжжя",
    "noon",
    "Мазепа",
]


# 1. Функція перевірки на паліндром
def is_palindrome(s):
    # Очищаємо рядок: переводимо в нижній регістр і прибираємо всі пробіли
    cleaned = s.lower().replace(" ", "")
    # Перевіряємо, чи дорівнює рядок самому собі у розвернутому вигляді
    return cleaned == cleaned[::-1]


# 2. Через filter + lambda знаходимо всі шифри (паліндроми)
ciphers = list(filter(lambda m: is_palindrome(m), messages))

# 3. Через map перетворюємо кожен шифр у потрібний формат рядка
formatted_ciphers = list(
    map(
        lambda m: f'🔐 {m} → {m.lower().replace(" ", "")}',
        ciphers,
    )
)

# 4. Виводимо результат
for item in formatted_ciphers:
    print(item)