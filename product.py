class Product:
    def __init__(self, name, quantity, purchase_price):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError

        if isinstance(quantity, int):
            self.quantity = quantity
        else:
            raise ValueError
        if isinstance(purchase_price, int):
            self.purchase_price = purchase_price
        else:
            raise ValueError
        self.payment_price = self.purchase_price + self.purchase_price * 0.25

    def show(self):
        return f"name:{self.name}\nquantity: {self.quantity}\n" \
               f"purchase price: {self.purchase_price}\npayment price: {self.payment_price}"


# p = Product("banan", 12, 1200)
# print(p.show())
