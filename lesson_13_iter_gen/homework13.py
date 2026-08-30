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