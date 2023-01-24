from models.warehouse import Warehouse


class Shop:
    def __init__(self):
        self._users = {}
        self._warehouse = Warehouse()

    def add_user(self, user):
        if user.username in self._users:
            print(f'The username "{user.username}" is already taken.')
            return
        self._users[user.username] = user

    def add_product(self, product):
        if product.seller.username not in self._users:
            print('This product has not signed seller.')
            return
        self._warehouse.add_product(product)

    def remove_product(self, product):
        if product not in self._warehouse:
            raise ValueError('Removing a product from the warehouse\n' + \
                             'which was not in the warehouse')
        self._warehouse.remove_product(product)

    def transaction(self, purchased):
        if purchased:
            if isinstance(purchased, list):
                for product in purchased:
                    product.seller.sell(product)
                    self.remove_product(product)
            else:
                purchased.seller.sell(purchased)
                self.remove_product(purchased)

    def show_all_products(self):
        print('--- SUPERMARKET-SUPERMARK ---')
        print('--------- WAREHOUSE ---------')
        print(self._warehouse)

    def show_all_users(self):
        print('--- SUPERMARKET-SUPERMARK ---')
        print('----------- USERS -----------')
        for user in self._users.values():
            print(user)