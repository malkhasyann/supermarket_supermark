class Cart:
    def __init__(self):
        self._products = []
        self._total_price = 0

    @property
    def total_price(self):
        return self._total_price

    def add_product(self, product):
        self._products.append(product)
        self._total_price += product.price

    def remove_product(self, product):
        self._products.remove(product)
        self._total_price -= product.price

    def __iter__(self):
        return iter(self._products)

    def __str__(self):
        return '\n'.join([str(product) for product in self._products]) + \
            f'Total: ${self.total_price}\n'
