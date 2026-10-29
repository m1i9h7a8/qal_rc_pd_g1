import json
from folklore_classes import FolkloreRecord, FieldExpedition

def merge_archives(filepaths: list) -> list:
    """Завантажує всі записи з усіх переданих JSON-файлів експедицій."""
    all_records = []
    for filepath in filepaths:
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            if "records" in data:
                for record_data in data["records"]:
                    all_records.append(FolkloreRecord.from_dict(record_data))
        except FileNotFoundError:
            print(f"⚠️ Попередження: Файл '{filepath}' не знайдено. Пропускаємо.")
        except json.JSONDecodeError:
            print(f"⚠️ Попередження: Файл '{filepath}' пошкоджений. Пропускаємо.")
    return all_records


def filter_records(records: list, genre: str = None, region: str = None, verified: bool = None) -> list:
    """Фільтрує список FolkloreRecord за заданими критеріями."""
    filtered = []
    for r in records:
        if genre is not None and r.genre.lower() != genre.lower():
            continue
        if region is not None and r.region.lower() != region.lower():
            continue
        if verified is not None and r.verified != verified:
            continue
        filtered.append(r)
    return filtered


def export_summary(records: list, filepath: str):
    """Зберігає у JSON-файл не повні записи, а лише короткі зведення."""
    summary_list = []
    for r in records:
        summary_list.append({
            "title": r.title,
            "genre": r.genre,
            "region": r.region,
            "verified": r.verified
        })
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(summary_list, f, indent=4, ensure_ascii=False)
    print(f"📊 Зведення успішно експортовано у файл '{filepath}' (всього записів: {len(summary_list)}).")


if __name__ == "__main__":
    print("=== КРОК 1: Створення 3 файлів експедицій ===")
    
    exp1 = FieldExpedition(1, "Дослідник А", "Диканька", "2026-05-10")
    exp1.add_record(FolkloreRecord("Ой у лузі червона калина", "пісня", "Полтавщина", "Ганна Остапенко", 1932, "Текст...", ["історична"], True))
    exp1.add_record(FolkloreRecord("Про лисицю та журавля", "казка", "Поділля", "баба Олена", 1954, "Казка...", ["дітям"], True))
    exp1.save("expedition_1.json")
    
    exp2 = FieldExpedition(2, "Дослідник Б", "Верховина", "2026-06-15")
    exp2.add_record(FolkloreRecord("Летіла зозуля", "пісня", "Полтавщина", "Микола С.", 1968, "Текст...", ["сумна"], True))
    exp2.add_record(FolkloreRecord("Легенда про Довбуша", "легенда", "Гуцульщина", "дід Михайло", 1980, "Текст...", ["Довбуш"], False))
    exp2.save("expedition_2.json")
    
    exp3 = FieldExpedition(3, "Дослідник В", "Охтирка", "2026-07-20")
    exp3.add_record(FolkloreRecord("Хліб — усьому голова", "прислів'я", "Слобожанщина", "дід Панас", 1985, "Зміст...", ["мудрість"], True))
    exp3.add_record(FolkloreRecord("Ой роду нашого красного", "пісня", "Полтавщина", "Анна М.", 2002, "Текст...", ["родина"], False))
    exp3.save("expedition_3.json")
    print("• Тестові файли експедицій створено успішно.\n")

    print("=== КРОК 2: Об'єднання через merge_archives() ===")
    files_list = ["expedition_1.json", "expedition_2.json", "expedition_3.json"]
    all_merged_records = merge_archives(files_list)
    print(f"• Загальна кількість об'єднаних записів: {len(all_merged_records)}\n")

    print("=== КРОК 3: Фільтрація перевірених записів з Полтавщини ===")
    filtered_records_list = filter_records(all_merged_records, region="Полтавщина", verified=True)
    print(f"• Знайдено відфільтрованих записів: {len(filtered_records_list)}")
    for record in filtered_records_list:
        print(f"  - {record}")
    print()

    print("=== КРОК 4: Збереження зведення через export_summary() ===")
    output_filepath = "summary_report.json"
    export_summary(filtered_records_list, output_filepath)