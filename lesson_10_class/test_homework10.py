import pytest
from homework10 import QuestRoom  # Імпортуємо ваш клас з файлу homework10.py

# --- ФІКСТУРИ (FIXTURES) ---
# Створюємо базову кімнату для тестів, щоб не дублювати код
@pytest.fixture
def base_room():
    return QuestRoom(name="Таємниці Єгипту", difficulty=4, limit=3)


# --- 1. ТЕСТИ КОНСТРУКТОРА ---
def test_constructor_initialization(base_room):
    """Перевірка правильної ініціалізації об'єкта класу."""
    assert base_room.name == "Таємниці Єгипту"
    assert base_room.difficulty == 4
    assert base_room.limit == 3
    assert base_room.players == []
    assert base_room.status == "waiting"
    assert base_room.events_log == []


# --- 2. ТЕСТИ ДОДАВАННЯ ГРАВЦІВ (add_player) ---
def test_add_single_player(base_room):
    """Додавання одного гравця — має бути у списку та в лозі."""
    base_room.add_player("Олег")
    assert "Олег" in base_room.players
    assert base_room.events_log[-1] == "Player Олег joined"

def test_add_multiple_players_order(base_room):
    """Додавання кількох гравців у правильному порядку."""
    base_room.add_player("Олег")
    base_room.add_player("Даша")
    assert base_room.players == ["Олег", "Даша"]

def test_add_player_over_limit(base_room):
    """Спроба додати гравця понад ліміт має повертати помилку."""
    base_room.add_player("Плеєр1")
    base_room.add_player("Плеєр2")
    base_room.add_player("Плеєр3")
    
    # Кімната заповнена (ліміт 3)
    result = base_room.add_player("Плеєр4")
    assert result == "No free slots!"
    assert len(base_room.players) == 3
    assert "Плеєр4" not in base_room.players


# --- 3. ТЕСТИ ВИЛУЧЕННЯ ГРАВЦІВ (remove_player) ---
def test_remove_existing_player(base_room):
    """Видалення існуючого гравця зі списку."""
    base_room.add_player("Олег")
    base_room.remove_player("Олег")
    assert "Олег" not in base_room.players
    assert base_room.events_log[-1] == "Player Олег left"

def test_remove_non_existing_player(base_room):
    """Спроба видалити гравця, якого немає в кімнаті."""
    base_room.add_player("Олег")
    result = base_room.remove_player("Ігор")
    assert result == "Player not found!"

def test_remove_from_empty_room(base_room):
    """Спроба видалити гравця з порожньої кімнати."""
    result = base_room.remove_player("Олег")
    assert result == "Player not found!"


# --- 4. ТЕСТИ ЗАПОВНЕНОСТІ (is_full, free_slots) ---
def test_room_filling_states(base_room):
    """Перевірка проміжних станів заповненості кімнати."""
    assert base_room.is_full() is False
    assert base_room.free_slots() == 3

    base_room.add_player("Олег")
    assert base_room.is_full() is False
    assert base_room.free_slots() == 2

    base_room.add_player("Даша")
    base_room.add_player("Іван")
    assert base_room.is_full() is True
    assert base_room.free_slots() == 0


# --- 5. ТЕСТИ ЗАПУСКУ КВЕСТУ (start) ---
def test_start_empty_room(base_room):
    """Спроба старту порожньої кімнати."""
    result = base_room.start()
    assert result == "Room is empty!"
    assert base_room.status == "waiting"

def test_start_successful(base_room):
    """Успішний старт гри з гравцями."""
    base_room.add_player("Олег")
    result = base_room.start()
    
    assert result == "Quest 'Таємниці Єгипту' started with 1 players!"
    assert base_room.status == "active"
    assert "Quest started" in base_room.events_log


# --- 6. ТЕСТИ СКИДАННЯ КІМНАТИ (reset_room) ---
def test_reset_room_logic(base_room):
    """Перевірка очищення списку, логування та фінального статусу."""
    base_room.add_player("Олег")
    base_room.start()
    
    result = base_room.reset_room()
    assert result == "Room reset!"
    assert base_room.players == []
    assert base_room.status == "waiting"
    assert "Room reset" in base_room.events_log


# --- 7. ТЕСТИ СПИСКУ ГРАВЦІВ (players_list) ---
def test_players_list_output(base_room):
    """Перевірка виводу списку гравців (текст vs список)."""
    assert base_room.players_list() == "No players in the room"
    
    base_room.add_player("Олег")
    assert base_room.players_list() == ["Олег"]


# --- 8. ТЕСТИ ЛОГУ ПОДІЙ (show_log) ---
def test_show_log_sequence(base_room):
    """Перевірка точного ланцюжка подій у лозі."""
    base_room.add_player("Олег")
    base_room.remove_player("Олег")
    base_room.add_player("Даша")
    base_room.start()
    
    expected_log = [
        "Player Олег joined",
        "Player Олег left",
        "Player Даша joined",
        "Quest started"
    ]
    assert base_room.show_log() == expected_log


# --- 9. КОМБІНОВАНІ СЦЕНАРІЇ ---
def test_combined_scenario_lifecycle(base_room):
    """Сценарій 1: Життєвий цикл кімнати (Додати -> Старт -> Скидання)."""
    base_room.add_player("Гравєць1")
    base_room.add_player("Гравєць2")
    base_room.start()
    assert base_room.status == "active"
    
    base_room.reset_room()
    assert base_room.status == "waiting"
    assert len(base_room.players) == 0
    assert "Room reset" in base_room.show_log()

def test_combined_scenario_slots_rotation(base_room):
    """Сценарій 2: Ротація місць при досягненні ліміту."""
    base_room.add_player("A")
    base_room.add_player("B")
    base_room.add_player("C")
    assert base_room.is_full() is True
    
    assert base_room.add_player("D") == "No free slots!"
    
    base_room.remove_player("B")
    assert base_room.is_full() is False
    
    base_room.add_player("E")
    assert base_room.players == ["A", "C", "E"]
    assert base_room.is_full() is True


# --- 🎁 БОНУСНІ ТЕСТИ (НА СТИК СТРЕС-ТЕСТІВ) ---
def test_performance_large_limit():
    """Тест на продуктивність: додавання 1000 гравців у велику кімнату."""
    large_room = QuestRoom("Мега Квест", 5, 1000)
    for i in range(1000):
        large_room.add_player(f"Player_{i}")
        
    assert len(large_room.players) == 1000
    assert large_room.is_full() is True
    assert len(large_room.events_log) == 1000
    assert large_room.events_log[500] == "Player Player_500 joined"

def test_multiple_resets_behavior(base_room):
    """Імітація подвійного скидання кімнати — чи не ламається логіка станів."""
    base_room.add_player("Олег")
    base_room.reset_room()
    
    # Повторне скидання порожньої кімнати
    result = base_room.reset_room()
    assert result == "Room reset!"
    assert base_room.status == "waiting"
    assert base_room.events_log[-1] == "Room reset"