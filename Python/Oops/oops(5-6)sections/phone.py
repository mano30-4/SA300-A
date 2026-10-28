from Python.Oops.oops_principles.items import Item

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