"""
Реалізувати функцію `sum_numbers_in_list(input_list)`, яка приймає список рядків, 
де кожен рядок містить числа, розділені комами. Функція повинна повертати список 
із сум чисел для кожного рядка або відповідне повідомлення про помилку у 
випадку некоректних даних.

#### **Приклади виклику функції:**
```python
sum_numbers_in_list(["1,2,3", "4,0,6"])  # [6, 10]
sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"])  # [6, "Не можу це зробити!", 10]
sum_numbers_in_list(["1,2,3,4", 7])  # [10, "Не можу це зробити! AttributeError"]
sum_numbers_in_list([])  # ValueError
sum_numbers_in_list("21")  # ValueError
```
"""


def sum_numbers_in_list(string_list: list):
    """Повертає список сум чисел зі списку строк,
    які складаються з чисел, розділених комою."""
 
    result = []
    for item in string_list:
        try:
            # 3. Перевірка типу: якщо елемент не є рядком
            if not isinstance(item, str):
                raise AttributeError()
                
            parts = item.split(',')
            current_sum = sum(int(num.strip()) for num in parts)
            result.append(current_sum)
            
        except ValueError:
            # 2. Обробка некоректних рядків
            result.append("Не можу це зробити!")
        except AttributeError:
            # 3. Обробка некоректних типів всередині списку
            result.append("Не можу це зробити! AttributeError")
    
    return result


if __name__ == "__main__":
    # Виклик 1: Коректне введення даних
    output = sum_numbers_in_list(["1,2,3", "4,0,6"])
    print(output)

    # Виклик 2: Некоректні рядки
    output = sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"])
    print(output)
    
    # Виклик 3: Некоректні типи всередині списку
    output = sum_numbers_in_list(["1,2,3,4", 7])
    print(output)

    # Виклик 4: Порожній список (безпечно перехоплюємо помилку та виводимо її назву)
    try:
        sum_numbers_in_list([])  
    except ValueError as e:
        print(e)

    # Виклик 5: Неправильний тип вхідних даних (безпечно перехоплюємо помилку та виводимо її назву)
    try:
        sum_numbers_in_list("21")  
    except ValueError as e:
        print(e)
    
    #sum_numbers_in_list(["1,2,3", "4,0,6"])  # [6, 10]
    #sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"])  # [6, "Не можу це зробити!", 10]
    #sum_numbers_in_list(["1,2,3,4", 7])  # [10, "Не можу це зробити! AttributeError"]
    #sum_numbers_in_list([])  # ValueError
    #sum_numbers_in_list("21")  # ValueError
    
