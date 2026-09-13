import re
import logging
from datetime import datetime

# Налаштування логування у файл hb_test.log
logging.basicConfig(
    filename='hb_test.log',
    level=logging.WARNING,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Регулярний вираз для точного парсингу вашого логу
LOG_PATTERN = re.compile(r'Timestamp\s+(?P<time>\d{2}:\d{2}:\d{2})\s+Key\s+(?P<key>[A-Z0-9]+)')

def log_reader(filepath):
    """Генератор для читання логу. Розвертає рядки хронологічно."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in reversed(lines):
            yield line.strip()

def parse_logs(lines):
    """Генератор, який парсить час та унікальний ключ з кожного рядка."""
    for line in lines:
        match = LOG_PATTERN.search(line)
        if match:
            data = match.groupdict()
            dt = datetime.strptime(data['time'], '%H:%M:%S')
            yield dt, data['key']

def analyze_heartbeats(log_file_path):
    """Аналізує інтервали heartbeat між процесами з унікальними ключами."""
    last_seen = {}
    
    lines = log_reader(log_file_path)
    parsed_data = parse_logs(lines)
    
    for current_time, key in parsed_data:
        if key in last_seen:
            prev_time = last_seen[key]
            duration = (current_time - prev_time).total_seconds()
            
            # Перевірка бізнес-вимог
            if 31 < duration <= 33:
                msg = f"Process {key}: Heartbeat interval was {duration}s"
                logging.warning(msg)
                print(f"[WARNING] {msg}")
                
            elif duration > 33:
                msg = f"Process {key}: Heartbeat interval breached critical limit! {duration}s"
                logging.error(msg)
                print(f"[ERROR] {msg}")
                
        last_seen[key] = current_time

if __name__ == "__main__":
    # Ім'я файлу з даними
    FILE_NAME = "hblog.txt" 
    
    # Автоматично знаходимо папку, в якій лежить сам скрипт
    script_dir = "/".join(__file__.replace("\\", "/").split("/")[:-1])
    # Формуємо повний шлях до hblog.txt у цій же папці
    LOG_FILE = f"{script_dir}/{FILE_NAME}" if script_dir else FILE_NAME
    
    print(f"Початок аналізу лог-файлу '{LOG_FILE}'...")
    analyze_heartbeats(LOG_FILE)
    print("Аналіз завершено. Результати записано в hb_test.log")