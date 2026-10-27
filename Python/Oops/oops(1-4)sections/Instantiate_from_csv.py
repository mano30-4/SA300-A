import csv
class Item():

  allItems=[] ## class Variable, a list to stores objects

  def __init__(self,name:str, price:float, quantity :int) :
    assert price>=0, "price can't be negative"
    assert quantity>0, "quantity can't be negative"
    self.name=name
    self.price=price
    self.quantity=quantity

    Item.allItems.append(self) # 'Item.' alias 'ClassName.' says we are referencing allitems which is Class Item
                              # if we use allitems. python wil search for it in funtion scope(__init__) then it will go for main class (global scope) but our list(variable) is in class Named 'Item' so we need to reference it so python searches there
  @classmethod
  def instantiate_from_csv(cls):
    with open('items.csv','r') as f:
       reader = csv.DictReader(f)
       items = list(reader)

    for item in items:
      Item(
        name = item.get('name'),
        price = float(item.get('price')),
        quantity=float(item.get('quantity'))
      )

  def __repr__(self):
    return f"Item('{self.name}',{self.price},{self.quantity})"


Item.instantiate_from_csv()

print(Item.allItems)
print(Item.allItems[0])