import functools
import logging
import random
import time

# Налаштовуємо формат логів, щоб на початку було слово INFO
logging.basicConfig(level=logging.INFO, format="INFO %(message)s")


def chronicle(scribe="Анонімний"):  # Якщо ім'я не передали, автоматично буде "Анонімний"
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            # Перетворюємо аргументи функції на рядок (наприклад: 'Атакувати', 'Перекоп')
            args_str = ", ".join([repr(a) for a in args])

            # Логуємо виклик функції
            logging.info(
                f"[Літописець: {scribe}] Викликано: {func.__name__}({args_str})"
            )

            # Запускаємо саму функцію та зберігаємо її результат
            result = func(*args)

            # Логуємо результат виконання
            logging.info(f"[Результат]: {result}")

            return result

        return wrapper

    return decorator


# --- Приклад використання ---


@chronicle("Самійло Величко")
def make_decision(action, target):
    return f"Рішення: {action} → {target}"


@chronicle()  # Порожні дужки — у лог піде дефолтне ім'я "Анонімний"
def count_warriors(regiment):
    return 500


# Виклик функцій для перевірки
make_decision("Атакувати", "Перекоп")
count_warriors("Полтавський")


logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")


def guard(secret):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Просимо користувача ввести пароль
            user_password = input("Назви пароль: ")

            # Перевіряємо, чи правильний пароль
            if user_password == secret:
                # Якщо правильний — логуємо як INFO та запускаємо функцію
                logging.info(f"Доступ надано: {func.__name__}")
                return func(*args, **kwargs)
            else:
                # Якщо неправильний — логуємо як WARNING, виводимо попередження і не запускаємо функцію
                logging.warning(f"Невдала спроба доступу до: {func.__name__}")
                print("Стій! Доступ заборонено.")
                return None

        return wrapper

    return decorator


# --- Приклад використання ---


@guard(secret="Мамай")
def open_treasury():
    print("Скарбниця відчинена!")
    return "золото, срібло, зброя"


# Запуск функції для перевірки
result = open_treasury()




# Налаштовуємо вивід логів (рівень логу та повідомлення)
logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")


def retry(times=3, delay=1.0):  # Задаємо значення за замовчуванням
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Цикл перебирає спроби від 1 до вказаної кількості (times)
            for attempt in range(1, times + 1):
                try:
                    # Намагаємося виконати функцію
                    result = func(*args, **kwargs)

                    # Якщо все добре — логуємо успіх і повертаємо результат
                    logging.info(f"Успіх на спробі {attempt}/{times}")
                    return result

                except Exception as error:
                    # Якщо виникла будь-яка помилка:

                    # Якщо це була ОСТАННЯ спроба — логуємо помилку і викидаємо її далі
                    if attempt == times:
                        logging.error(
                            f"Усі {times} спроб вичерпано. Останній збій: {error}"
                        )
                        raise error  # Повторно піднімаємо виняток, як вимагає умова

                    # Якщо спроби ще є — логуємо попередження і чекаємо перед наступною
                    logging.warning(
                        f"Спроба {attempt}/{times} не вдалася: {error}"
                    )
                    time.sleep(delay)  # Затримка в секундах

        return wrapper

    return decorator


# --- Приклад використання ---


@retry(times=4, delay=0.5)
def unreliable_scout():
    if random.random() < 0.7:  # 70% шанс провалу для тесту
        raise ConnectionError("Розвідник не повернувся")
    return "Ворог за річкою!"


# Запуск функції
try:
    result = unreliable_scout()
    print(result)
except ConnectionError:
    print("Програма завершилась помилкою, бо всі спроби провалено.")
