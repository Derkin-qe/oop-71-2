class Hero:
    def __init__(self, name: str, level: int, health: int, strength: int):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def attack(self):
        print(f"{self.name} наносит удар!")
        self.strength -= 1

    def rest(self):
        print(f"{self.name} отдыхает…")
        self.health += 1


# --- Проверка работы (Дополнительное требование) ---

# 1. Создаем 2 объекта класса Hero
hero1 = Hero(name="Арагорн", level=5, health=10, strength=8)
hero2 = Hero(name="Гэндальф", level=10, health=12, strength=5)

# 2. Вызываем методы для первого героя и проверяем изменение параметров
print("=== Тестирование Героя 1 ===")
hero1.greet()
print(f"Статы до атаки: Сила = {hero1.strength}")
hero1.attack()
print(f"Статы после атаки: Сила = {hero1.strength}\n")

# 3. Вызываем методы для второго героя и проверяем изменение параметров
print("=== Тестирование Героя 2 ===")
hero2.greet()
print(f"Статы до отдыха: Здоровье = {hero2.health}")
hero2.rest()
print(f"Статы после отдыха: Здоровье = {hero2.health}\n")
