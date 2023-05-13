from product import Product
from store import Store
from database import Data

file = 'store_base.json'
file1 = 'bank.json'
dt = Data()
st = Store(dt, file, file1)

if __name__ == "__main__":
    print("Welcome to the Store Management System!")
    while True:
        action = input("Enter the action 'add', 'sell', 'output','sort','exit': ")
        if action == 'exit':
            break
        elif action == 'add':
            name = input("Enter product name: ")
            quantity = int(input("Enter the quantity of product: "))
            purchase_price = int(input("Enter purchase price: "))
            prod = Product(name, quantity, purchase_price)
            st.enter_a_product(prod)
        elif action == 'sell':
            name = input("Enter product name: ")
            quantity = int(input("Enter the quantity of product: "))
            st.sell_product(name, quantity)
        elif action == 'output':
            st.display_stock_balance()
        elif action == 'sort':
            st.sort_products()
        else:
            print("Invalid action. Please try again.")
