"""x = lambda a: a**2 + 10
print(x(9))"""




"""car_brand = ("Ford", "Migrella", "Suzuki")
list = iter(car_brand)

print(next(list))
print(next(list))
print(next(list))

myname = "I am so proud of you"
myit = iter(myname)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))"""

class Interest:
  def __init__(self, truth, dare):
    self.truth = truth
    self.dare = dare

  def option(self):
    print("choose whatever you like!")

class hobby:
  def __init__(self, singing, dancing):
    self.singing = singing
    self.dancing = dancing

  def option(self):
    print("I dont like both")

class Luck:
  def __init__(self, bad, good):
    self.bad = bad
    self.good =good

  def option(self):
    print("Fly!")

m1 = Interest("eeee", "hhhh")       
p1 = hobby("deded", "fefef") 
l1 = Luck("efefe", "ef2ee2d")     

for x in (m1,p1,l1):
  x.option()