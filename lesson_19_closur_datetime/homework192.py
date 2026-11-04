import re
from datetime import datetime

# =====================================================================
# Завдання 1. Фабрика перетворювачів напруги
# =====================================================================

def make_voltage_converter(factor: float):
    """Створює функцію, яка множить напругу на коефіцієнт."""
    def converter(volts: float) -> float:
        return volts * factor
    return converter


# =====================================================================
# Завдання 2. Лічильник електроенергії
# =====================================================================

def make_electricity_meter(address: str, initial_kwh: float = 0.0):
    """Створює лічильник зі спільним станом для трьох функцій."""
    current_kwh = initial_kwh

    def add(kwh: float) -> float:
        nonlocal current_kwh  # дозволяє змінювати значення ззовні
        current_kwh += kwh
        return current_kwh

    def reset() -> float:
        nonlocal current_kwh
        current_kwh = initial_kwh
        return current_kwh

    def report() -> str:
        return f"Адреса: {address} | Спожито: {current_kwh} кВт·год"

    return add, reset, report


# =====================================================================
# Завдання 3. Диспетчер аварійних подій
# =====================================================================

def make_dispatcher(station_name: str):
    """Формує повідомлення та передає його у вказану функцію-callback."""
    def dispatch(event: str, callback):
        message = f"[{station_name}] {event}"
        callback(message)  # викликаємо функцію, яку нам передали
    return dispatch

# Обробники (callbacks)
def log_to_console(message: str):
    print(message)

def log_to_file(message: str):
    with open("dispatch_log.txt", "a", encoding="utf-8") as f:
        f.write(message + "\n")


# =====================================================================
# Завдання 4. Сортування підстанцій
# =====================================================================

def make_sorter(field: str, reverse: bool = False):
    """Повертає функцію, яка сортує список за вказаним ключем."""
    def sorter(data_list: list) -> list:
        return sorted(data_list, key=lambda item: item[field], reverse=reverse)
    return sorter


# =====================================================================
# БЛОК ПЕРЕВІРКИ (ЗАПУСК УСІХ ЗАВДАНЬ)
# =====================================================================
if __name__ == "__main__":
    print("--- Перевірка Завдання 1 ---")
    step_up = make_voltage_converter(10.0)   # підвищувальний
    step_down = make_voltage_converter(0.5)  # знижувальний

    print(step_up(22.0))     # 220.0
    print(step_down(220.0))  # 110.0
    print(step_up(11.0))     # 110.0
    print()

    print("--- Перевірка Завдання 2 ---")
    add, reset, report = make_electricity_meter("вул. Франка, 12", 150.0)

    print(add(30.5))    # 180.5
    print(add(14.0))    # 194.5
    print(report())     # Адреса: вул. Франка, 12 | Спожито: 194.5 кВт·год
    print(reset())      # 150.0
    print(report())     # Адреса: вул. Франка, 12 | Спожито: 150.0 кВт·год
    print()

    print("--- Перевірка Завдання 3 ---")
    dispatch = make_dispatcher("Підстанція №7 Івано-Франківськ")

    dispatch("Перевищення напруги", log_to_console)
    dispatch("Коротке замикання", log_to_console)
    dispatch("Відновлення живлення", log_to_file)
    print("(Повідомлення про відновлення живлення записано в файл dispatch_log.txt)")
    print()

    print("--- Перевірка Завдання 4 ---")
    substations = [
        {"name": "Підстанція №3", "region": "Коломия",        "load_kw": 4500},
        {"name": "Підстанція №7", "region": "Івано-Франківськ", "load_kw": 8200},
        {"name": "Підстанція №1", "region": "Калуш",           "load_kw": 3100},
        {"name": "Підстанція №9", "region": "Надвірна",        "load_kw": 6700},
    ]

    sort_by_load = make_sorter("load_kw", reverse=True)
    for s in sort_by_load(substations):
        print(s["name"], s["load_kw"])

    print("-" * 20)

    sort_by_name = make_sorter("name")
    for s in sort_by_name(substations):
        print(s["name"])