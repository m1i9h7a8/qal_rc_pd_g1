class MagicCreature:

    def __init__(self, name: str, magic_level: int, health: float):
        # Заборона створення екземпляру самого базового класу
        if type(self) is MagicCreature:
            raise TypeError(
                "Неможливо створити екземпляр абстрактного класу MagicCreature безпосередньо!"
            )

        self.name = name

        # Звертаємось до сеттерів, які автоматично перевірять значення та створять змінні
        self.magic_level = magic_level
        self.health = health

        # Статус життя визначається початковим здоров'ям
        self.__alive = health > 0

    # ==========================================
    # PROPERTY (ГЕТТЕРИ ТА СЕТТЕРИ)
    # ==========================================
    @property
    def magic_level(self) -> int:
        return self._magic_level

    @magic_level.setter
    def magic_level(self, level: int):
        # Валідація прямо в сеттері
        if not (1 <= level <= 10):
            raise ValueError("Рівень магії має бути від 1 до 10!")
        self._magic_level = level

    @property
    def health(self) -> float:
        return self.__health

    @health.setter
    def health(self, hp: float):
        # Валідація прямо в сеттері
        if not (0 <= hp <= 100):
            raise ValueError("Здоров'я має бути від 0 до 100!")

        self.__health = hp

        # Якщо здоров'я падає до 0, істота вмирає
        if self.__health == 0:
            self.__alive = False

    @property
    def is_alive(self) -> bool:
        return self.__alive

    # ==========================================
    # МЕТОДИ КЛАСУ
    # ==========================================
    def take_damage(self, amount: float):
        if not self.__alive:
            return f"{self.name} вже переміг смерть... або ні."

        # Зменшуємо здоров'я, але не нижче 0
        new_health = max(0.0, self.__health - amount)
        self.health = (
            new_health  # Сеттер сам оновить __alive, якщо здоров'я стане 0
        )

    def __str__(self) -> str:
        return f"{self.name} | Магія: {self.magic_level} | HP: {self.health} | Живий: {self.is_alive}"

    # ==========================================
    # ІМІТАЦІЯ АБСТРАКТНИХ МЕТОДІВ
    # ==========================================
    def use_ability(self):
        raise NotImplementedError(
            "Субклас повинен реалізувати метод use_ability()"
        )

    def describe(self) -> str:
        raise NotImplementedError(
            "Субклас повинен реалізувати метод describe()"
        )

# ==========================================
# 1. КЛАС MOLFAR (МОЛЬФАР)
# ==========================================
class Molfar(MagicCreature):

    def __init__(
        self, name: str, magic_level: int, health: float, element: str, spells: int
    ):
        # Викликаємо конструктор базового класу MagicCreature
        super().__init__(name, magic_level, health)
        self.element = element
        self.spells = spells  # Викличе сеттер для перевірки

    @property
    def spells(self) -> int:
        return self.__spells

    @spells.setter
    def spells(self, value: int):
        if value < 0:
            raise ValueError("Запас заклинань не може бути від'ємним!")
        self.__spells = value

    def use_ability(self) -> str:
        if self.spells > 0:
            self.spells -= 1
            return f"Мольфар {self.name} закликає {self.element}! Залишилось заклинань: {self.spells}"
        return (
            f"Мольфар {self.name} виснажений — сила стихій покинула його!"
        )

    def describe(self) -> str:
        return f"Мольфар {self.name}, повелитель стихії {self.element}. Рівень магії: {self.magic_level}"


# ==========================================
# 2. КЛАС RUSALKA (РУСАЛКА)
# ==========================================
class Rusalka(MagicCreature):

    def __init__(
        self, name: str, magic_level: int, health: float, river: str, charm_power: int
    ):
        super().__init__(name, magic_level, health)
        self.river = river
        self.charm_power = charm_power  # Викличе сеттер для перевірки

    @property
    def charm_power(self) -> int:
        return self.__charm_power

    @charm_power.setter
    def charm_power(self, value: int):
        if not (1 <= value <= 5):
            raise ValueError("Сила чар має бути в діапазоні від 1 до 5!")
        self.__charm_power = value

    def use_ability(self) -> str:
        msg = f"Русалка {self.name} з річки {self.river} зачаровує мандрівника! Сила чар: {self.charm_power}"
        if self.charm_power == 5:
            msg += " Ніхто не встоїть!"
        return msg

    def describe(self) -> str:
        return f"Русалка {self.name}, мешканка річки {self.river}. Сила чар: {self.charm_power}/5"


# ==========================================
# 3. КЛАС PERELESNYK (ПЕРЕЛЕСНИК)
# ==========================================
class Perelesnyk(MagicCreature):

    def __init__(
        self, name: str, magic_level: int, health: float, speed: int, form: str = "вогняна куля"
    ):
        super().__init__(name, magic_level, health)
        self.speed = speed  # Викличе сеттер для перевірки
        
        # Перевірка початкової форми (за замовчуванням "вогняна куля")
        if form not in ["вогняна куля", "людська"]:
            form = "вогняна куля"
        self.form = form

    @property
    def speed(self) -> int:
        return self.__speed

    @speed.setter
    def speed(self, value: int):
        if not (1 <= value <= 100):
            raise ValueError("Швидкість польоту має бути від 1 до 100!")
        self.__speed = value

    def change_form(self) -> str:
        if self.form == "вогняна куля":
            self.form = "людська"
        else:
            self.form = "вогняна куля"
        return f"Перелесник перетворився на {self.form}!"

    def use_ability(self) -> str:
        msg = f"Перелесник {self.name} мчить крізь ніч зі швидкістю {self.speed}! Форма: {self.form}"
        if self.form == "людська":
            msg += " Ніхто не здогадається..."
        return msg

    def describe(self) -> str:
        return f"Перелесник {self.name}. Швидкість: {self.speed}. Зараз у формі: {self.form}"

class EnchantedForest:

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.__creatures = []  # Приватний список для зберігання об'єктів істот

    # ==========================================
    # PROPERTY
    # ==========================================
    @property
    def creatures_count(self) -> int:
        # Рахуємо лише живих істот у лісі
        return sum(1 for c in self.__creatures if c.is_alive)

    # ==========================================
    # МЕТОДИ КЛАСУ
    # ==========================================
    def add_creature(self, creature: MagicCreature) -> str:
        # 1. Перевірка на місткість лісу
        if len(self.__creatures) >= self.capacity:
            return f"Зачарований ліс {self.name} переповнений!"

        # 2. Перевірка, чи жива істота
        if not creature.is_alive:
            return "Мертві істоти не можуть оселитись у лісі!"

        # 3. Перевірка, чи істота вже є у лісі (за ім'ям)
        for existing_creature in self.__creatures:
            if existing_creature.name == creature.name:
                return f"{creature.name} вже мешкає у цьому лісі!"

        # Якщо всі перевірки пройдено — додаємо
        self.__creatures.append(creature)
        return f"{creature.name} успішно оселився у лісі {self.name}."

    def remove_creature(self, name: str) -> str:
        for creature in self.__creatures:
            if creature.name == name:
                self.__creatures.remove(creature)
                return f"{name} залишив ліс {self.name}."
        return f"Істоту {name} не знайдено у лісі!"

    def most_powerful(self):
        if not self.__creatures:
            return "Ліс порожній — нема кому чаклувати!"

        # Знаходимо істоту з максимальним рівнем магії
        # (якщо рівні однакові, max() поверне першу знайдену)
        return max(self.__creatures, key=lambda c: c.magic_level)

    def attack_intruder(self, intruder_name: str):
        # Шукаємо тільки ЖИВИХ істот, які можуть атакувати
        live_creatures = [c for c in self.__creatures if c.is_alive]

        if not live_creatures:
            return f"Ліс беззахисний перед {intruder_name}!"

        # Збираємо результати use_ability() від кожної живої істоти
        battle_log = [c.use_ability() for c in live_creatures]
        return battle_log

    def census(self):
        if not self.__creatures:
            return "Ліс порожній"

        # Збираємо опис усіх істот у лісі
        return [c.describe() for c in self.__creatures]

forest = EnchantedForest("Чорний Ліс", capacity=5)

molfar = Molfar("Юрій", magic_level=8, health=90, element="вогонь", spells=3)
rusalka = Rusalka("Калина", magic_level=6, health=100, river="Дніпро", charm_power=5)
perelesnyk = Perelesnyk("Іскра", magic_level=7, health=85, speed=95, form="вогняна куля")

forest.add_creature(molfar)
forest.add_creature(rusalka)
forest.add_creature(perelesnyk)

print(forest.most_powerful())
print(forest.attack_intruder("мисливець"))

molfar.take_damage(90)
print(molfar.is_alive)

print(forest.census())