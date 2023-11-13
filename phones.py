from item import Item
#New class phone inheritance from item
#item is the parent class and phone one child class
class Phones(Item):
  class_all=[]
  #call super function to have acces to all atributes and methods.
  def __init__(self,name: str,price:float,quantity: int, broken_ph:int):
    super().__init__(
        name, price, quantity
    )
    #run validations
    assert broken_ph>=0, f"broken_ph {broken_ph} needs to be non-negative"

    #Objects
    self.broken_ph=broken_ph

    #Save the phones instances only
    self.class_all.append(self)