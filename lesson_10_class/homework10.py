class QuestRoom:
    """Клас для моделювання квестової кімнати."""

    def __init__(self, name: str, difficulty: int, limit: int):
        self.name = name                  # Назва кімнати
        self.difficulty = difficulty      # Рівень складності (1–5)
        self.limit = limit                # Ліміт гравців
        self.players = []                 # Список гравців, що увійшли
        self.status = "waiting"           # Початковий стан кімнати
        self.events_log = []              # Лог подій (історія)

    def add_player(self, name: str):
        """Додає гравця до кімнати, якщо є вільні місця."""
        if len(self.players) >= self.limit:
            return "No free slots!"
        
        self.players.append(name)
        self.events_log.append(f"Player {name} joined")

    def remove_player(self, name: str):
        """Видаляє гравця зі списку."""
        if name not in self.players:
            return "Player not found!"
        
        self.players.remove(name)
        self.events_log.append(f"Player {name} left")

    def is_full(self) -> bool:
        """Повертає True, якщо кімната заповнена, інакше — False."""
        return len(self.players) == self.limit

    def free_slots(self) -> int:
        """Повертає кількість вільних місць у кімнаті."""
        return self.limit - len(self.players)

    def start(self) -> str:
        """Запускає квест, якщо в кімнаті є гравці."""
        if not self.players:
            return "Room is empty!"
        
        self.status = "active"            # Переводимо стан у "active"
        self.events_log.append("Quest started")
        return f"Quest '{self.name}' started with {len(self.players)} players!"

    def reset_room(self) -> str:
        """Очищає список гравців та скидає стан кімнати."""
        self.status = "finished"          # Змінює стан на "finished"
        self.players.clear()              # Очищає список гравців
        self.status = "waiting"           # Ставить стан "waiting"
        self.events_log.append("Room reset")
        return "Room reset!"

    def players_list(self):
        """Повертає список імен гравців або повідомлення, якщо кімната пуста."""
        if not self.players:
            return "No players in the room"
        return self.players

    def show_log(self) -> list:
        """Повертає історію всіх подій (лог)."""
        return self.events_log

    def __str__(self) -> str:
        """Красиве текстове представлення кімнати."""
        return f"QuestRoom: {self.name} | Difficulty: {self.difficulty} | Players: {len(self.players)}/{self.limit}"


# --- БЛОК ДЛЯ ПЕРЕВІРКИ РОБОТИ ПРОГРАМИ ---
if __name__ == "__main__":
    print("--- 1. Створення кімнати та початковий стан ---")
    # Створюємо кімнату "Піратський острів" з рівнем 3 та лімітом 2 гравці
    room = QuestRoom("Піратський острів", 3, 2)
    print(room)
    print(f"Поточний статус: {room.status}")
    print(f"Список гравців: {room.players_list()}")
    print(f"Вільних місць: {room.free_slots()}")

    print("\n--- 2. Додавання гравців та перевірка ліміту ---")
    room.add_player("Олег")
    room.add_player("Даша")
    print(room)
    print(f"Чи заповнена кімната? {room.is_full()}")
    # Пробуємо додати третього гравця, коли ліміт 2
    print(f"Спроба додати третього: {room.add_player('Максим')}")

    print("\n--- 3. Старт гри ---")
    print(room.start())
    print(f"Статус під час гри: {room.status}")

    print("\n--- 4. Видалення гравців ---")
    # Спроба видалити того, кого немає
    print(f"Видалення відсутнього: {room.remove_player('Аліса')}")
    room.remove_player("Олег")
    print(f"Список після видалення Олега: {room.players_list()}")

    print("\n--- 5. Скидання кімнати (Рестарт) ---")
    print(room.reset_room())
    print(f"Статус після скидання: {room.status}")
    print(f"Список гравців після скидання: {room.players_list()}")

    print("\n--- 6. Перегляд логу подій (Історія) ---")
    for event in room.show_log():
        print(f"📝 {event}")