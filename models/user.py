from models.cart import Cart

class User:
    def __init__(self, username, money):
        self.username = username
        self.money = money
        self._cart = Cart()
        self._selling_products = Cart()

    @property
    def username(self):
        return self._username

    @property
    def money(self):
        return self._money

    @username.setter
    def username(self, value):
        if len(value) < 2:
            raise ValueError('Username length has to be at least 2.')
        self._username = value

    @money.setter
    def money(self, value):
        if value <= 0:
            raise ValueError('User amount cannot be less than or equal 0.')
        self._money = value

    def add_product_to_cart(self, product):
        self._cart.add_product(product)

    def remove_product_from_cart(self, product):
        self._cart.remove_product(product)

    def add_selling_product(self, product):
        self._selling_products.add_product(product)

    def remove_selling_product(self, product):
        self._selling_products.remove_product(product)

    def purchase(self, product):
        if self.username == product.seller.username:
            print(f'{self.username} wants to buy his/her own product... CANCELLED')
            return
        if self.money < product.price:
            print('The transaction is cancelled due to insufficient amount of money.')
            return
        self.money -= product.price
        print(f'{self.username} purchased {product.name}')

    def sell(self, product):
        self.money += product.price
        self.remove_selling_product(product)

    def show_cart(self):
        print(f'{self.username}\'s shopping cart:\n')
        print(f'{self._cart}')

    def __str__(self):
        return 'USER:\n' + \
            f'\tUsername: {self.username}\n' + \
            f'\tMoney: {self.money:.2f}\n'
