class House:
    def __init__(self, name, number_of_floors):
        # Инициализируем атрибуты объекта
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        # Проверка на допустимость этажа
        if 0 < new_floor <= self.number_of_floors:
            # Вывод последовательности чисел от 1 до new_floor
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            # Сообщение об ошибке
            print("Такого этажа не существует")

    def __str__(self):
        return f"Название: {self.name}, количество этажей: {self.number_of_floors}"
    def __len__(self):
        return self.number_of_floors

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

#  Выводим на консоль строки
# __str__
print(h1)
print(h2)


print(len(h1))
print(len(h2))