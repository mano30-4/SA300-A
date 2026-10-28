import csv

class Item():
    all = []
    def __init__(self, name: str, price: float, quantity: int):
        assert price >= 0, "price can't be negative"
        assert quantity > 0, "quantity can't be negative"
        self.__name = name
        self.price = price
        self.quantity = quantity
    # storing list of objects that are created
        Item.all.append(self)

    ''' ## read only attribute '_variable' (work around) 
        disadvantage -> _varaible can be updated 
        @property
        def name(self):
            return self._name
    '''
    #@property -- getters
    ## __variable is not accessible from outside class
    @property
    def name(self):
        return self.__name

    @name.setter # reference to getter under @property
    def name(self,value):
        if len(value) > 10 :
            raise Exception("too long")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.price * self.quantity

    def __repr__(self):
        return f"{self.__class__.__name__}({self._name}, {self.price}, {self.quantity}"

    @classmethod
    def instantiate_from_csv(cls):
        with open('../oops(1-4)sections/items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=float(item.get('quantity'))
            )
