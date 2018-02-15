
class Product():

  def __init__(self, price, item_name, weight, brand, status):
    self.price = price
    self.item_name = item_name
    self.weight = weight
    self.brand = brand
    self.status = status
  
  def sell(self): #changes status to 'sold'
    print self.item_name + " is SOLD OUT"
    self.status = 'SOLD'
    return self

  def add_tax(self, tax): #takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
    print ("Taxed by this amount: " + str(tax))
    self.price = self.price * tax + self.price
    return self

  '''takes reason for return as a parameter and change status accordingly. 
  If the item is being returned because it is defective, change status to "defective" and change price to 0.
  If it is being returned in the box, like new, mark it "for sale".
  If the box has been opened, set the status to "used" and apply a 20% discount.'''

  def returnItem(self, reason): 
    print ("Item has been returned")
    if reason == 'defective':
      self.status = 'DEFECTIVE'
      self.price = 0
    elif reason == "Returned like new":
      self.status = "FOR SALE"
    elif reason == "Box has been opened":
      self.status = "USED"
      self.price *= .80
      return self

  def displayInfo(self):
    print "Price: $" + str(self.price)
    print "Item name: " + str(self.item_name)
    print "Weight: " + str(self.weight) + 'lbs'
    print "Brand: " + str(self.brand)
    print "Status: " + str(self.status)
    return self

myproduct = Product(199.99, "Headphone", 1, "Bose", "Sale")
myproduct.sell()
myproduct.displayInfo()
myproduct.returnItem("defective")
myproduct.displayInfo()

newproduct = Product(45, "cellphones", 3, "Samsung", "Sale")
newproduct.returnItem("Returned like new")
newproduct.displayInfo()



  
