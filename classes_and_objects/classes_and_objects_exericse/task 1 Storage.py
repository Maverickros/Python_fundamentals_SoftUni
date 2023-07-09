class Storage:
    storage = []   # това се отнася за целия клас   - клас атрибут

    def __init__(self,capacity):
        self.capacity = capacity
    # добавяме add product
    def add_product(self, product: str):
        if self.capacity > 0: # по този начин разбираме дали има място в склада
            self.capacity -= 1 # изваждаме от свободното място
            Storage.storage.append(product) # извикваме класа а после атрибута и добавяме продукта

    def get_products(self):
        return Storage.storage





storage = Storage(4)
storage.add_product("apple")
storage.add_product("banana")
storage.add_product("potato")
storage.add_product("tomato")
storage.add_product("bread")
print(storage.get_products())
