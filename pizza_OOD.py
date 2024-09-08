class Topping:

    def __init__(self, name: str, type: str, price: float):
        self.name = name
        self.type = type
        self.price = price

class Pizza:

    def __init__(self, size="m", crust="round", sauce="pizza", toppings = []):
        self.size = size
        self.crust = crust
        self.sauce = sauce
        self.toppings = toppings

    def add_topping(self, topping: Topping):
        self.toppings.append(topping)
    
    def remove_topping(self, topping: Topping):
        new_tops = []
        for top in self.toppings:
            if top != topping:
                new_tops.append(top)

        self.toppings = new_tops

    def calculate_price(self) -> int:
        price = 0
        if self.size == "s":
            price += 6.99
        elif self.size == "m":
            price += 8.99
        elif self.size == "l":
            price += 10.99
        
        for top in self.toppings:
            price += top.price
        
        return price

pepp = Topping("pepperoni", "meat", 1.99)
olive = Topping("olive", "veg", 0.99)

pizza1 = Pizza()
pizza1.add_topping(pepp)
pizza1.add_topping(olive)
print(pizza1.calculate_price())
