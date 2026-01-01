class Product:
    def operation(self):
        pass

class ConcreteProductA(Product):
    def operation(self):
        return "Result of ConcreteProductA"

class ConcreteProductB(Product):
    def operation(self):
        return "Result of ConcreteProductB"

class Factory:
    def create_product(self, type_: str) -> Product:
        if type_ == 'A':
            return ConcreteProductA()
        elif type_ == 'B':
            return ConcreteProductB()
        else:
            raise ValueError(f"Unknown product type: {type_}")
