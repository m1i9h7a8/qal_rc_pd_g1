class ChainOfOrders:
    def __init__(self, people):
        # Перетворюємо список людей на стандартний ітератор
        self.people_iter = iter(people)
        # Одразу беремо першу людину (якщо список порожній — буде None)
        self.current = next(self.people_iter, None)

    def __iter__(self):
        return self 

    def __next__(self):
        # Якщо людей не було взагалі або ланцюжок закінчився
        if self.current is None:
            raise StopIteration
        
        # Намагаємося взяти НАСТУПНУ людину через next()
        next_person = next(self.people_iter, None)
        
        if next_person is not None:
            # Якщо наступна людина є — передаємо далі
            message = f"{self.current} каже {next_person}: передай далі!"
            self.current = next_person  # Поточна стає наступною для наступного кроку
        else:
            # Якщо наступної людини немає — ланцюжок завершено
            message = f"{self.current} каже: теля прив'язав!"
            self.current = None  # Сигнал для завершення на наступному кроці
            
        return message

# Перевірка
chain = ChainOfOrders(["Дід", "Батько", "Михайлик", "Василько"])

for message in chain:
    print(message)


def village_rumor(start_message, people):
    
    current_rumor = start_message

    for i in range(len(people)):
        person = people[i]
        
        # Визначаємо дієслово: для першої людини "каже", для інших "переказує"
        action = "каже" if i == 0 else "переказує"
        
        # Повертаємо поточний стан чутки через yield
        yield f'{person} {action}: "{current_rumor}"'
        
        # Модифікуємо чутку для НАСТУПНОЇ людини
        if i == len(people) - 2:
            # Якщо наступна людина остання, додаємо фінальну фразу
            current_rumor = f"{current_rumor} (переказала {person}) (і всі дізналися!)"
        else:
            # Для всіх інших випадків просто додаємо ім'я того, хто переказав
            current_rumor = f"{current_rumor} (переказала {person})"

for version in village_rumor("Теля втекло!", ["Горпина", "Параска", "Явдоха", "Оксана"]):
    print(version)

ivents = [
    "Михайлик передав доручення",
    "Василько відмовився",
    "Грицько передав доручення",
    "Оленка прив'язала теля",
    "Данилко передав доручення",
]

count = sum(1 for ev in ivents if "передав доручення" in ev and ev.split()[0])

print(f"Доручення передавали {count} рази")


import itertools

def toloka_queue(workers):
    if not workers:
        return
        
    # itertools.cycle нескінченно повторює елементи списку по колу
    for worker in itertools.cycle(workers):
        yield f"Черга: {worker}"

# --- Перевірка роботи ---
queue = toloka_queue(["Іван", "Марія", "Степан"])

# Беремо рівно 7 чергувань з нескінченного генератора
for turn in itertools.islice(queue, 7):
    print(turn)

def find_calf(log):
    for line in log:
        # Перевіряємо обидва варіанти дієслова в рядку
        if "прив'язав" in line or "прив'язала" in line:
            yield line
            return  # Зупиняє генератор відразу після першої знахідки

# --- Перевірка роботи ---
journal = [
    "Михайлик отримав доручення",
    "Михайлик передав Василькові",
    "Василько загрався",
    "Василько передав Оленці",
    "Оленка прив'язала теля біля хліва",
    "Оленка пішла додому",
    "Дід заспокоївся",
]

# Використовуємо next(), щоб отримати лише перший знайдений рядок
result = next(find_calf(journal))
print(result)