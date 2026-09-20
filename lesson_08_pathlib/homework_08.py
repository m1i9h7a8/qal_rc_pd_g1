### Робота з файлами та папками — завдання
"""
1. **Створення файлу**
   Створи текстовий файл `hello.txt` і запиши в нього рядок:

   ```
   Hello, Python!
   ```
"""
# coding here
from pathlib import Path
with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("Hello, Python!\n")



"""
2. **Читання файлу**
   Відкрий файл `hello.txt` і виведи його вміст на екран.
"""
# coding here
with open("hello.txt", "r", encoding="utf-8") as f:
   content = f.read()
print(content)

"""   
3. **Дозапис у файл**
   Додай у файл `hello.txt` ще один рядок:

   ```
   Learning file operations.
   ```
"""
# coding here
with open("hello.txt", "a", encoding="utf-8") as f:
    f.write("Learning file operations.\n")
    


"""
4. **Читання кількох рядків**
   Виведи всі рядки з файлу `hello.txt` по одному рядку (без додаткових символів `\n`).
"""
# coding here
with open("hello.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

"""
5. **Підрахунок символів**
   Прочитай файл `hello.txt` і виведи кількість символів у ньому.
"""
# coding here
with open("hello.txt", "r", encoding="utf-8") as f:
    print(f"Кількість символів у файлі: {len(f.read())}")

"""
6. **Створення папки**
   Створи папку з назвою `data`. Усередині неї створи файл `notes.txt` із текстом:

   ```
   My first note.
   ```
"""
# coding here
new_directory = Path(r"C:\Users\Misha2\Desktop\Course\qal_rc_pd_g1\lesson_08_pathlib\data")
new_directory.mkdir(parents=True, exist_ok=True)
file_path = new_directory / "notes.txt"
with open(file_path, "w", encoding="utf-8") as f:
    f.write("My first note.\n")



"""
7. **Список файлів у папці**
   Виведи на екран список усіх файлів у папці `data`.
"""
# coding here
files = [f for f in new_directory.iterdir() if f.is_file()]

# Виведення списку всіх файлів
print("Список всіх файлів:")
for file in files:
    print(file)

"""
8. **Копіювання вмісту**
   Прочитай вміст файлу `notes.txt` і запиши його у файл `copy.txt` (у тій же папці `data`).
"""
# coding here

source_file = new_directory / "notes.txt"
destination_file = new_directory / "copy.txt"

with open(source_file, "r", encoding="utf-8") as f:
    content = f.read()
    print(f"Вміст файлу notes.txt: {content}")

with open(destination_file, "w", encoding="utf-8") as f:
      f.write(content + "\n")
with open(destination_file, "r", encoding="utf-8") as f:
    copy_content = f.read()
print(f"Вміст файлу copy.txt: {copy_content}")


"""
9. **Об’єднання файлів**
   Створи два файли: `a.txt` і `b.txt`, кожен із будь-яким текстом.
   Запиши їхній вміст у новий файл `ab.txt`.
"""
# coding here

file_path = new_directory / "a.txt"
with open(file_path, "w", encoding="utf-8") as f:
    f.write("My note in file a.txt.\n")
file_path = new_directory / "b.txt"
with open(file_path, "w", encoding="utf-8") as f:
    f.write("My note in file b.txt.\n")

file_ab_path = new_directory / "ab.txt"

with open(new_directory / "a.txt", "r", encoding="utf-8") as f:
    text_a = f.read()

with open(new_directory / "b.txt", "r", encoding="utf-8") as f:
    text_b = f.read()

with open(file_ab_path, "w", encoding="utf-8") as f:
    f.write(text_a + text_b)
with open(file_ab_path, "r", encoding="utf-8") as f:
    text_a_b = f.read()

print("Файли 'a.txt' та 'b.txt' успішно об'єднані у файл 'ab.txt'!") 
print(f"Вміст файлу ab.txt: \n{text_a_b}")

"""
10. **Пошук слова у файлі**
    У файлі `notes.txt` перевір, чи є слово `"note"`.
    Якщо є — виведи `"Знайдено"`, інакше `"Не знайдено"`.
"""
# coding here

file_to_search = new_directory / "notes.txt"
with open(file_to_search, "r", encoding="utf-8") as f:
    file_content = f.read()
if "note" in file_content:
    print("Знайдено")
else:
    print("Не знайдено")
