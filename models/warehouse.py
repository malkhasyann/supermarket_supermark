class Warehouse:
    def __init__(self):
        self._products = []

    def add_product(self, product):
        self._products.append(product)

    def remove_product(self, product):
        self._products.remove(product)

    def __contains__(self, item):
        return item in self._products

    def __str__(self):
        return '\n'.join([str(product) for product in self._products])