from models.user import User
from models.product import Product
from models.shop import Shop


if __name__ == '__main__':
    shop = Shop()

    user1 = User('Ashtarak Kat', 10_000)

    user1.show_cart()
    user1.show_selling_products()

    shop.add_user(user1)
    smetana = Product('Smetana', 500, user1)
    shop.add_product(user1.add_selling_product(smetana))

    user1.show_cart()
    user1.show_selling_products()

    shop.show_all_products()
    print()
    shop.show_all_users()

    user2 = User('Nargiz', 2400)
    shop.add_user(user2)
    user2.add_product_to_cart(smetana)

    print(user2)
    user2.show_cart()

    shop.transaction(user2.purchase(smetana))

    print(user1)
    print(user2)

    shop.show_all_products()

    user3 = User('Nargiz', 7000)

    shop.add_user(user3)

    user4 = User('մթերային', 5000)
    shop.add_user(user4)

    p1 = Product('zeytun', 15.5, user4, 'hamov a')
    p2 = Product('havi dosh', 10, user4, '')
    p3 = Product('hac', 1, user4, 'sev boqon')

    shop.add_product(user4.add_selling_product(p1))
    shop.add_product(user4.add_selling_product(p2))
    shop.add_product(user4.add_selling_product(p3))

    user5 = User('Erem', 24)
    shop.add_user(user5)

    user5.add_product_to_cart(p1)
    user5.add_product_to_cart(p2)
    user5.add_product_to_cart(p2)

    shop.transaction(user5.purchase_all_cart())

    shop.show_all_users()
    shop.show_all_products()