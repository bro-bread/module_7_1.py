import os

class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)
    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    def __init__(self, filename='products.txt.txt'):
        self.filename = filename

    def get_products(self):
        with open(self.filename, encoding='utf-8') as file:
            content = file.read()
            print(content)

    def add(self, *products):
        file2 = open(self.filename, "r+")
        t2x2 = file2.read()
        for er in products:
            er2 = str(er.name)
            if er.name in t2x2:
                print("Продукт ", er2," уже есть в магазине'")
            else:
                if type(er) == Product:
                    file2 = open(self.filename, "a")
                    bate = os.path.getsize('products.txt.txt')
                    file2.seek(bate)
                    file2.write("\n")
                    file2.write(er2)
                    file2.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())