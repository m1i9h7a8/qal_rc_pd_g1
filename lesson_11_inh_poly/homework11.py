class Cossack:
    def __init__(self, name, kurin, weapons=None):
        self.name = name
        self.kurin = kurin
        # Використовуємо None як дефолтне значення, щоб уникнути проблеми з mutable аргументами
        self.weapons = weapons if weapons is not None else []
        self.victories = 0

    def arm(self, weapon):
        if weapon in self.weapons:
            return f"{self.name} вже має {weapon}!"
        self.weapons.append(weapon)

    def win_battle(self, enemy):
        self.victories += 1
        return f"{self.name} переміг {enemy}! Слава козаку!"

    def __str__(self):
        weapons_str = ", ".join(self.weapons) if self.weapons else "немає зброї"
        return f"Козак {self.name} | Курінь: {self.kurin} | Перемоги: {self.victories} | Зброя: {weapons_str}"


class ZaporozhianSich:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cossacks = []

    def enlist(self, cossack):
        if len(self.cossacks) >= self.capacity:
            return "Січ переповнена!"
        
        # Перевіряємо, чи немає вже козака з таким самим об'єктом або ім'ям
        for c in self.cossacks:
            if c.name == cossack.name:
                return f"{cossack.name} вже на Січі!"
                
        self.cossacks.append(cossack)

    def dismiss(self, name):
        for cossack in self.cossacks:
            if cossack.name == name:
                self.cossacks.remove(cossack)
                return f"Козака {name} відпущено з Січі."
        return f"Козака {name} не знайдено!"

    def call_to_battle(self, enemy):
        if not self.cossacks:
            return "Нікому боронити Січ!"
        return f"Військо Запорозьке виступає проти {enemy}! У поході {len(self.cossacks)} козаків!"

    def best_warrior(self):
        if not self.cossacks:
            return "Січ порожня!"
        
        # Збройовий алгоритм пошуку козака з макс. перемогами
        best = max(self.cossacks, key=lambda c: c.victories)
        return best

    def roster(self):
        if not self.cossacks:
            return "На Січі нікого немає"
        return [cossack.name for cossack in self.cossacks]


cossack = Cossack("Іван Сірко", "Кальміуський")

cossack.arm("шабля")
cossack.arm("мушкет")
print(cossack.win_battle("яничари"))
print(cossack)