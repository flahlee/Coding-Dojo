class Bike(object):

  def __init__(self, price, max_speed, miles):
    self.price = price
    self.max_speed = max_speed
    self.miles = miles


  def displayInfo(self):
      print ("The bike's price is $" + str(self.price))
      print ("Maximum speed is " + str(self.max_speed) + 'mph')
      print ("The total miles is " + str(self.miles) + 'miles')


  def ride(self):
      print "Riding"
      self.miles += 10

  def reverse(self):
      print "Reversing"
      self.miles -= 5


#first instance ride three times, reverse once and have it displayinfo()
bike1 = Bike(150, 10, 0)
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

#second instance ride twice, reverse twice and have it displayinfo()
bike2 = Bike(240, 15, 0)
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

#third instance reverse three times and displayinfo()
bike3 = Bike(350, 10, 20)
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()
