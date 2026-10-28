
class Item():
    all = []
    def __init__(self, name: str, price: float, quantity: int):
        assert price >= 0, "price can't be negative"
        assert quantity > 0, "quantity can't be negative"
        self.name = name
        self.price = price
        self.quantity = quantity
    # storing list of objects that are created
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.quantity}"


#phone1 = Item("Jcphone",500,5)
#phone2 = Item("jcphone10",700,5)
'''suppose u want to have special variable to know no of broken phones in quantity
 we have, broken phones count is not required for very Item we create item could be anything'''

"""So either we create special variable every time we create a new version of phone 
and keep track of it creating special variable every time for it"""

#phone1 = Item("Jcphone",500,5)
#phone1.broken_phones= 2
#phone2 = Item("jcphone10",700,5)
#phone2.broken_phones = 3

""" Or Create phone class and use inheritance 
Here we want to have same initialization as 'Item' class but in addition to it we want have broken_phones count
1) simple way :
just copy code of 'Item' initialisation and broken_phones variable 
imagine u have new product with versions and u want keep track of colour this time 
with increase of this kinda tracking for different products
using simple way creates too much duplication which is not good practise
2) use super function :
lets u extend custom use case without duplication 
"""

'''
#simple way:
class phone(Item):
    all=[]
    def __init__(self, name: str, price: float, quantity: int, broken_phones: int = 0):
        # validation
        assert quantity > 0, f"Quantity = {quantity} can't be negative"
        assert price >= 0, f" price ={price} can't be negative"
        assert broken_phones >= 0, f"broken phones = {broken_phones} can't be negative"

        # assignment
        self.name = name
        self.price = price
        self.quantity = quantity
        self.broken_phones = broken_phones

        #storing list of objects that are created
        phone.all.append(self)

phone1 = phone("JCphone", 500, 5 ,3)
phone2 = phone("JCphone10",700,5,2)
'''
class phone(Item):
    def __init__(self, name: str, price: float, quantity: int, broken_phones: int = 0):
        # calling super function to have access to all variables / methods
        super().__init__(name,price,quantity)
        # validation
        assert broken_phones >= 0, f"broken phones = {broken_phones} can't be negative"
        # assignment
        self.broken_phones = broken_phones

phone1 = phone("JCphone", 500, 5 ,3)
print(phone1.calculate_total_price())
phone2 = phone("JCphone10",700,5,2)

print(Item.all)
print(phone.all)


