import json


class Data:

    def read_products(self, filename):
        with open(filename, 'r') as file:
            return json.load(file)

    def write_products(self, data, filename):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
