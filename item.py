import csv
class Item():
  #class atributes
  pay_rate=0.9
  all=[]
  #class atributes can be defined for the class outside
  #like item.pay_rate=0.6
  def __init__(self,name: str,price:float,quantity: int):
    #Run validations
    assert price>=0, f"Price {price} needs to be non-negative"
    assert quantity>=0, f"Quantity {quantity} needs to be non-negative"
    #assign self objects
    self.__name=name
    self.quantity=quantity
    self.price=price
    #Save the instances that has been created.
    Item.all.append(self)
    print(f"{self.__name} fue creado")
  @property
  def name_read_only(self):
    return self.__name
  #Now if you want to set the atrbiute that we put in just read mode
  #We can use @name.setter as example like:
  @name_read_only.setter
  def name_setter(self,value):
    #we can put some adivce like:
    print(f"You set the atribute {value}")
    self.__name=value
  def total_value(self):
    return self.price*self.quantity
  def apply_discount(self):
    self.price=self.price*self.pay_rate

  #__repr__ representing self objects like the description.
  #In the item.all
  def __repr__(self):
    # return f"Item('{self.name}',{self.price},{self.quantity})"
    return f"{self.__class__.__name__}('{self.__name}',{self.price},{self.quantity})"
  #You can get the instances from a csv file.
  #the @classmethod decorator will make Python pass the class of the instance it's called on as the first argument
  @classmethod
  def instantiate_from_csv(cls):
    with open("item.csv","r") as f:
      reader=csv.DictReader(f)
      items=list(reader)
      for i in items:
        Item(
            name=i.get("name"),
            price=float(i.get("price")),
            quantity=int(i.get("quantity"))
            )


  #The staticmethod never get the object as the first component.
  # the @staticmethod can be used to define a factory method that
  # returns class instances. It is unable to return a class object.
  #The isinstance() function checks if the object (first argument)
  #is an instance or subclass of classinfo class (second argument).
  @staticmethod
  def is_integer(num):
    if isinstance(num,float):
      return num.is_integer()
    elif isinstance(num,int):
      return True
    else:
      return False

Item0=Item("Obj1",100,3)
Item1=Item("Phone android",180,3)

print("Hola")