from abc import ABC
from typing import List, Optional


class Flower(ABC):
    def __init__(self, name: str, color: str, stem_length: float, cost: float, freshness_days: int):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.cost = cost
        self.freshness_days = freshness_days

    def __repr__(self):
        return f'{self.name}({self.color}, {self.stem_length} см, {self.cost} руб, свеж {self.freshness_days} дн.)'


class Rose(Flower):
    def __init__(self, color: str, stem_length: float, cost: float, freshness_days: int):
        super().__init__('Роза', color, stem_length, cost, freshness_days)


class Tulip(Flower):
    def __init__(self, color: str, stem_length: float, cost: float, freshness_days: int):
        super().__init__('Тюльпан', color, stem_length, cost, freshness_days)


class Lily(Flower):
    def __init__(self, color: str, stem_length: float, cost: float, freshness_days: int):
        super().__init__('Лилия', color, stem_length, cost, freshness_days)


class Bouquet:
    def __init__(self, flowers: Optional[List[Flower]] = None):
        self.flowers: List[Flower] = flowers if flowers is not None else []

    def add_flower(self, flower: Flower):
        self.flowers.append(flower)

    def total_cost(self) -> float:
        return sum(flower.cost for flower in self.flowers)

    def average_wilting_time(self) -> float:
        if not self.flowers:
            return 0.0
        return sum(flower.freshness_days for flower in self.flowers) / len(self.flowers)

    def sort_by_freshness(self):
        self.flowers.sort(key=lambda f: f.freshness_days, reverse=True)

    def sort_by_color(self):
        self.flowers.sort(key=lambda f: f.color)

    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda f: f.stem_length)

    def sort_by_cost(self):
        self.flowers.sort(key=lambda f: f.cost)

    def find_flowers_by_freshness(self, min_freshness: int) -> List[Flower]:
        return [flower for flower in self.flowers if flower.freshness_days >= min_freshness]

    def find_flowers_by_color(self, target_color: str) -> List[Flower]:
        return [flower for flower in self.flowers if flower.color.lower() == target_color.lower()]

    def find_flowers_by_stem_length_range(self, min_length: float, max_length: float) -> List[Flower]:
        return [flower for flower in self.flowers if min_length <= flower.stem_length <= max_length]


rose1 = Rose('Красный', 50.3, 150.0, 5)
rose2 = Rose('Белый', 45.0, 140.2, 4)
tulip1 = Tulip('Жёлтый', 30.8, 60.0, 3)
tulip2 = Tulip('Розовый', 35.0, 73.3, 4)
lily1 = Lily('Белый', 60.0, 200.99, 6)

bouquet = Bouquet()
bouquet.add_flower(rose1)
bouquet.add_flower(rose2)
bouquet.add_flower(tulip1)
bouquet.add_flower(tulip2)
bouquet.add_flower(lily1)

print('Исходный букет:')
for f in bouquet.flowers:
    print(f)
print(f'Общая стоимость: {bouquet.total_cost():.2f} руб')
print(f'Среднее время жизни букета: {bouquet.average_wilting_time():.2f} дней\n')

bouquet.sort_by_freshness()
print('Сортировка по свежести цветов (от свежих к менее свежим):')
for f in bouquet.flowers:
    print(f)
print()

fresh_flowers = bouquet.find_flowers_by_freshness(5)
print(f'Цветы со свежестью >= 5 дней: {len(fresh_flowers)} шт.')
for f in fresh_flowers:
    print(f)
print()

stem_length = bouquet.find_flowers_by_stem_length_range(40, 55)
print(f'Цветы с подходящей длиной стебля:')
for f in stem_length:
    print(f)
print()

bouquet.sort_by_color()
print('Сортировка по цвету (алфавитный порядок):')
for f in bouquet.flowers:
    print(f)
print()
