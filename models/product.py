class Product:
    def __init__(self, name, price, seller, description=''):
        self.name = name
        self.price = price
        self.description = description
        self._seller = seller

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def description(self):
        return self._description

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def seller(self):
        return self._seller

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError('Product price cannot be less than or equal 0.')
        self._price = value

    @description.setter
    def description(self, value):
        self._description = value

    def __str__(self):
        return 'PRODUCT:\n' + \
            f'\tName: {self.name}\n' + \
            f'\tPrice: {self.price}\n' + \
            f'\tSeller: {self.seller.username}\n' + \
            f'\tDescription: {self.description or "-"}\n'
