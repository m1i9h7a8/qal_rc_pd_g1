# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1
    
    # Complete the while loop condition.
    while multiplier <= 25:
        result = number * multiplier
        # десь тут помилка, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def summa(a,b):
    return a + b
a = (input("Введіть a: "))
b = (input("Введіть b: "))
result = summa(a,b)
print(f"Результат суми: {result}")



# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def serednearifm(list_of_numbers):
    return sum(list_of_numbers) / len(list_of_numbers)
user_input = input("Введіть числа через пробіл: ")
list_of_numbers = [int(x) for x in user_input.split()]
seredne = serednearifm(list_of_numbers)
print(f"Середнє арифметичне: {seredne}")



# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def zvorot(ryadok):
    return ryadok[::-1]
ryadok_input = input("Введіть рядок через пробіл: ")
zvorot_ryadok = zvorot(ryadok_input)
print(f"рядок у зворотному порядку:{zvorot_ryadok}")


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def maxlenword(spysok_sliv):
        return max(spysok_sliv, key=len)
user_input = input("Введіть слова через пробіл: ")
words_list = user_input.split()
if not words_list:
    print("Ви не ввели жодного слова!")
else:
    longest_word = maxlenword(words_list)
    print(f"Найдовше слово у списку: {longest_word}")



# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    for i in range(len1 - len2 + 1):
         if str1[i : i + len2] == str2:
            return i 
    return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7 
#вивід різних форматів числа - у двійковій, восьмирічний, шістнадцятковий системах
def preobrazovka(chislo):
    dviykova = bin(chislo)
    vosmerychna = oct(chislo)
    shistnadcyatkova = hex(chislo)
    
    return dviykova, vosmerychna, shistnadcyatkova

user_num = int(input("Введіть число: "))

bin_res, oct_res, hex_res = preobrazovka(user_num)

print(f"Двійкова: {bin_res}")
print(f"Восьмерична: {oct_res}")
print(f"Шістнадцяткова: {hex_res}")


# task 8
#Обчисліть площу кола з радіусом radius. Використайте значення π = 3.14159
def ploscha(radius):
    pi = 3.14159
    s = pi * (radius**2)
    return s
user_radius = float(input("Введіть радіус кола: "))

result = ploscha(user_radius)

print(f"Площа кола з радіусом {user_radius} дорівнює: {result:.2f}")


# task 9
#пошук унікальних елементів
def get_unique_elements(input_list):
    return set(input_list)
user_input = input("Введіть слова або числа через пробіл: ")
words_list = user_input.split()
print(f"Унікальні елементи: {', '.join(get_unique_elements(words_list))}")

# task 10
#калькулятор

def calculate_all_operations(num1, num2):
    """Виконує всі базові арифметичні операції для двох чисел."""
    plus = num1 + num2
    minus = num1 - num2
    multi = num1 * num2
    div = num1 / num2
    floor_div = num1 // num2
    modulo = num1 % num2
    power = num1 ** num2
    
    return plus, minus, multi, div, floor_div, modulo, power
a = float(input("Введіть перше число (наприклад, 17): ").replace(",", "."))
b = float(input("Введіть друге число (наприклад, 5): ").replace(",", "."))
res_plus, res_minus, res_multi, res_div, res_floor, res_mod, res_pow = calculate_all_operations(a, b)

print(f"\n--- Результати операцій для чисел {a} та {b} ---")
print(f"Додавання: {a} + {b} = {res_plus:.4f}")
print(f"Віднімання: {a} - {b} = {res_minus:.4f}")
print(f"Множення: {a} * {b} = {res_multi:.4f}")
print(f"Ділення: {a} / {b} = {res_div:.4f}")
print(f"Цілочисельне ділення: {a} // {b} = {res_floor:.4f}")
print(f"Залишок від ділення: {a} % {b} = {res_mod:.4f}")
print(f"Піднесення до степеня: {a} ** {b} = {res_pow:.4f}")

"""Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обов'язково документуйте функції та дайте зрозумілі імена змінним."""