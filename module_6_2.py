class Vehicle:
    __COLOR_VARIANTS = ('metalic', 'red', 'yellow', 'black', 'white')

    def __init__(self, owner , model, engine_power, color ):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model (self):
        return f'Модель: {self.__model}'
    def get_horsepower (self):
        return f'Мощность двигателя: {self.__engine_power}'
    def get_color (self):
        return f'Цвет: {self.__color}'
    def print_info (self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print('Владелец', self.owner)

    def set_color (self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Sergey','Nissan', 300, 'black')
vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('RED')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()