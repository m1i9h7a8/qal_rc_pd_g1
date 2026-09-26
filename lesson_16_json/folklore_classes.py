import json

class FolkloreRecord:
    def __init__(self, title: str, genre: str, region: str, narrator: str, 
                 year: int, content: str, tags: list, verified: bool):
        self.title = title
        self.genre = genre
        self.region = region
        self.narrator = narrator
        self.year = year
        self.content = content
        self.tags = tags
        self.verified = verified

    def to_dict(self) -> dict:
        """Повертає словник із усіма атрибутами об'єкта."""
        return {
            "title": self.title,
            "genre": self.genre,
            "region": self.region,
            "narrator": self.narrator,
            "year": self.year,
            "content": self.content,
            "tags": self.tags,
            "verified": self.verified
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Класовий метод, що створює об'єкт FolkloreRecord зі словника."""
        return cls(
            title=data["title"],
            genre=data["genre"],
            region=data["region"],
            narrator=data["narrator"],
            year=data["year"],
            content=data["content"],
            tags=data["tags"],
            verified=data["verified"]
        )

    def __str__(self) -> str:
        """Повертає гарно відформатований рядок із інформацією про запис."""
        return f"[{self.genre}] \"{self.title}\" — {self.region}, {self.year} (оповідач: {self.narrator})"


class FieldExpedition:
    def __init__(self, expedition_id: int, researcher: str, location: str, date: str):
        self.expedition_id = expedition_id
        self.researcher = researcher
        self.location = location
        self.date = date
        self.records = []  # Список об'єктів FolkloreRecord

    def add_record(self, record: FolkloreRecord):
        """Додає об'єкт FolkloreRecord до списку, перевіряючи дублікати за назвою."""
        for r in self.records:
            if r.title == record.title:
                return f"Запис '{record.title}' вже є в експедиції"
        self.records.append(record)
        return f"Запис '{record.title}' успішно додано."

    def remove_record(self, title: str):
        """Видаляє запис за назвою."""
        for r in self.records:
            if r.title == title:
                self.records.remove(r)
                return f"Запис '{title}' видалено."
        return f"Запис '{title}' не знайдено"

    def find_by_genre(self, genre: str) -> list:
        """Повертає список усіх записів заданого жанру."""
        return [r for r in self.records if r.genre.lower() == genre.lower()]

    def to_dict(self) -> dict:
        """Повертає словник експедиції, де записи конвертуються у словники."""
        return {
            "expedition_id": self.expedition_id,
            "researcher": self.researcher,
            "location": self.location,
            "date": self.date,
            "records": [r.to_dict() for r in self.records]
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Класовий метод, що відновлює об'єкт експедиції разом із вкладеними об'єктами."""
        expedition = cls(
            expedition_id=data["expedition_id"],
            researcher=data["researcher"],
            location=data["location"],
            date=data["date"]
        )
        for record_data in data.get("records", []):
            expedition.records.append(FolkloreRecord.from_dict(record_data))
        return expedition

    def save(self, filepath: str):
        """Зберігає експедицію у JSON-файл."""
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=4, ensure_ascii=False)

    @classmethod
    def load(cls, filepath: str):
        """Класовий метод для завантаження експедиції з файлу з обробкою помилок."""
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            return cls.from_dict(data)
        except FileNotFoundError:
            print(f"Помилка: Файл '{filepath}' не знайдено.")
            return None
        except json.JSONDecodeError:
            print(f"Помилка: Не вдалося розпарсити JSON у файлі '{filepath}' (пошкоджений формат).")
            return None