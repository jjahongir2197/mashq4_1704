class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, percent):
        discount = self.price * percent / 100
        self.price -= discount

    def show_product(self):
        print(self.name, "-", self.price)


class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def apply_discount_all(self, percent):
        for product in self.products:
            product.apply_discount(percent)

    def show_products(self):
        for product in self.products:
            product.show_product()


def main():
    p1 = Product("Telefon", 2000000)
    p2 = Product("Laptop", 8000000)

    shop = Shop()

    shop.add_product(p1)
    shop.add_product(p2)

    shop.apply_discount_all(10)

    shop.show_products()


main()
