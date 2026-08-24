class QuestRoom:
    def __init__(self, name: str, difficulty: int, limit: int):
        self.name = name
        self.difficulty = difficulty
        self.limit = limit
        self.players = []
        self.status = "waiting"
        self.events_log = []

    def add_player(self, name: str):
        if len(self.players) >= self.limit:
            return "No free slots!"
        self.players.append(name)
        self.events_log.append(f"Player {name} joined")

    def remove_player(self, name: str):
        if name not in self.players:
            return "Player not found!"
        self.players.remove(name)
        self.events_log.append(f"Player {name} left")

    def is_full(self) -> bool:
        return len(self.players) == self.limit

    def free_slots(self) -> int:
        return self.limit - len(self.players)

    def start(self) -> str:
        if not self.players:
            return "Room is empty!"
        self.status = "active"
        self.events_log.append("Quest started")
        return f"Quest '{self.name}' started with {len(self.players)} players!"

    def reset_room(self) -> str:
        self.status = "finished"
        self.players.clear()
        self.status = "waiting"
        self.events_log.append("Room reset")
        return "Room reset!"

    def players_list(self):
        if not self.players:
            return "No players in the room"
        return self.players

    def show_log(self) -> list:
        return self.events_log

    def __str__(self) -> str:
        return f"QuestRoom: {self.name} | Difficulty: {self.difficulty} | Players: {len(self.players)}/{self.limit}"

if __name__ == "__main__":
    print("--- Старт тесту класу QuestRoom ---")
    
   #room = QuestRoom("Піратський острів", 3, 4)

    room = QuestRoom("Піратський острів", 3, 4)
    print(room)  # Виведе інформацію о кімнаті через __str__
    
    # 2. Додаємо гравців
    room.add_player("Олег")
    room.add_player("Даша")
    
    # 3. Запускаем квест и выводим результат метода start()
    print(room.start())  
    print(f"Статус кімнаты післе старта: {room.status}")
    print(room)
    
    # 4. Перевіряєм нові методи (Завдання 2)
    print(f"Вільних місць: {room.free_slots()}")
    print(f"Кімната заповнена? {room.is_full()}")
    print(f"Список гравців: {room.players_list()}")
    
    # 5. Пробуємо видалити гравця
    print(room.remove_player("Максим")) # Напишет "Player not found!"
    room.remove_player("Олег")
    print(f"Список післе видалення Олега: {room.players_list()}")
    
    # 6. Сброс кімнаты та вивід логів
    print(room.reset_room())
    print("Історія подій (Лог):")
    for event in room.show_log():
        print(f"  -> {event}")

