import logging


class ShoppingCart:
    logging.basicConfig(level=logging.DEBUG)

    def __init__(self) -> list[str]:
        self.basket_list = []

    def add_items(self, item: list[str]) -> list[str]:
        self.basket_list.append(item)

    def get_items(self):
        return self.basket_list

    def quantity_count(self):
        return len(self.basket_list)

    def total_items_price(self, quantity: dict) -> float:
        total_price = 0.0
        for item in self.basket_list:
            price = quantity.get(item)
            total_price += price
        return total_price


basket = ShoppingCart()
basket.add_items("apple")
basket.add_items("orange")

print(f"Basket contains items of : \t{basket.get_items()}")
print(f"Total item quantity is : \t{basket.quantity_count()}")

Total = basket.total_items_price( {
    "orange": 1.0,
    "apple": 2.0
})
print(f"Total price is : \t{Total}")

# total_count = ShoppingCart.quantity_count()
# print(total_count)

list_cars = ["maruthi", "bmw", "volvo", "audi", "benz", "FORD"]

add_top_list_cars = [car.upper() for car in list_cars if "bmw" in list_cars]
print(add_top_list_cars)
