import random


class Store:
    def __init__(self, data, fname, fname2):
        self.data = data
        self.fname = fname
        self.fname2 = fname2
        self.products = data.read_products(self.fname)
        self.account = data.read_products(self.fname2)
        self.balance = self.account['balance']
        self.profit = self.account['profit']
        if self.balance == 0:
            self.add_balance()

    def enter_a_product(self, obj):
        print(f"Your balance: {self.balance}")
        if obj.name not in self.products:
            self.products[obj.name] = {'quantity': obj.quantity,
                                       'purchase_price': obj.purchase_price,
                                       'payment_price': obj.payment_price}
            self.data.write_products(self.products, self.fname)
        else:
            self.products[obj.name]['quantity'] += obj.quantity
            if self.products[obj.name]['purchase_price'] == obj.purchase_price:
                self.data.write_products(self.products, self.fname)
            else:
                self.products[obj.name]['purchase_price'] = obj.purchase_price
                self.products[obj.name]['payment_price'] = obj.purchase_price + (obj.purchase_price * 0.25)
                self.data.write_products(self.products, self.fname)
        self.balance -= (self.products[obj.name]['quantity'] * self.products[obj.name]['purchase_price'])
        self.account['balance'] = self.balance
        self.data.write_products(self.account, self.fname2)
        print(f"Your balance after buying: {self.balance}")

    def add_balance(self):
        self.balance = random.randint(2000000, 10000000)
        self.balance = self.balance / 10
        self.balance = round(self.balance) * 10

    def check_prod(self, name):
        if self.products[name]['quantity'] == 0:
            del self.products[name]

    def sell_product(self, name, quantity):
        if isinstance(name, str) and isinstance(quantity, int):
            print(f"Your balance before selling: {self.balance}")
            if name not in self.products:
                raise ValueError("The product does not exist")
            else:
                if quantity > self.products[name]['quantity']:
                    raise ValueError("To much quantity of product")
                else:
                    self.products[name]['quantity'] -= quantity
                    self.balance += quantity * self.products[name]['payment_price']
                    self.data.write_products(self.products, self.fname)
                    self.account['balance'] = self.balance

                    self.profit = self.account['profit']
                    self.account['profit'] += (self.products[name]['payment_price'] - self.products[name][
                        'purchase_price']) * \
                                              quantity
                    self.data.write_products(self.account, self.fname2)
                    self.check_prod(name)
                    self.data.write_products(self.products, self.fname)
                    print(f"Your balance after selling: {self.balance}")
                    print(f"Your profit after selling product: {self.account['profit']}")
        else:
            raise ValueError


    def sort_products(self):
        sorted_products = dict(sorted(self.products.items(), key=lambda x: x[1]['quantity']))
        self.data.write_products(sorted_products, self.fname)
        print("Product are sorted by quantity !!!")


    def display_stock_balance(self):
        for k, v in self.products.items():
            print(f"{k}")
            print(f"{v}")

        # if __name__ == '__main__':
#     d = Data()
#     s = Store(d, 'base.json')
#     prod = Product("banan", 12, 350)
#     prod2 = Product("kiwi", 1, 500)
#     s.enter_a_product(prod)
#     s.enter_a_product(prod2)
#     #print(s.products['kiwi']['quantity'])
