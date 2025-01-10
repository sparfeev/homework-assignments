from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'Название: {self.name}; Вес: {self.weight};Категория: {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'


    def get_products(self):
        file = open(self.__file_name, 'r')
        product = file.read()
        file.close()
        return product

    def add(self, *product):
        for product in product:
            if product.name not in self.get_products():
                file = open(self.__file_name, 'a')
                file.write(product.__str__() + '\n')
                file.close()
            else:
                print(f'Продукт {product.name} уже был в магазине, его общий вес теперь равен ')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
s1.add(p1, p2, p3)
s1.get_products()
print(p1)
print(p2)
print(p3)