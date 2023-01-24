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
        if self.username == product.seller.username:
            print(f'{self.username}, you can not add your selling product\n' + \
                  'to your shopping cart.')
        self._cart.add_product(product)

    def remove_product_from_cart(self, product):
        self._cart.remove_product(product)

    def add_selling_product(self, product):
        self._selling_products.add_product(product)
        return product

    def remove_selling_product(self, product):
        self._selling_products.remove_product(product)
        return product

    def purchase(self, product):
        if self.username == product.seller.username:
            print(f'{self.username} wants to buy his/her own product... CANCELLED')
            return None
        if self.money < product.price:
            print('The transaction is cancelled due to insufficient amount of money.')
            return None
        self.money -= product.price
        print(f'{self.username} purchased {product.name}')
        return product

    def purchase_all_cart(self):
        if self.money < self._cart.total_price:
            print('The transaction is cancelled due to insufficient amount of money.')
            return None
        temp = [product for product in self._cart]
        for product in temp:
            self.purchase(product)
            self._cart.remove_product(product)
        print(f'{self.username} purchased all the products from his/her shopping cart.')
        return temp

    def sell(self, product):
        self.money += product.price
        self.remove_selling_product(product)

    def show_cart(self):
        print(f'{self.username}\'s shopping cart:\n')
        print(self._cart)

    def show_selling_products(self):
        print(f'{self.username}\'s selling products:\n')
        print(self._selling_products)

    def __str__(self):
        return 'USER:\n' + \
            f'\tUsername: {self.username}\n' + \
            f'\tMoney: ${self.money:.2f}\n'
