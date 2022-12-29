class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def find(self, product_name):
        for el in self.products:
            if el.name == product_name:
                return el

    def remove(self, product_name):
        for el in self.products:
            if el.name == product_name:
                self.products.remove(el)

    def __repr__(self):
        result = []
        for el in self.products:
            result.append(f"{el.name}: {el.quantity}")

        return '\n'.join(result)