"""# class
class day7:
    x=1
    print(x)
class day8:
    y=9
    print(y)
class day78(day7,day8):
    def __init__(self):
       self.z=self.x+self.y
c=day78()
print(c.z)
    
"""
"""class A:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class B(A):
  def __init__(self, fname, lname,address):

    A.__init__(self, fname, lname)
    address=self.address
  def printaddress(self):
     print(self.address)
class C(B):
  def __init__(self,fname,lname,address):

     B.__init__self(self,fname,lname,address)
  
x = B("Prami", "Olsen")
y=C("jjjfj")
x.printname()
y.printaddress()"""
"""class A:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class B(A):
    def __init__(self, fname, lname, address):
        super().__init__(fname, lname)  # or A.__init__(self, fname, lname)
        self.address = address  # corrected assignment
    
    def printaddress(self):
        print(self.address)

class C(B):
    def __init__(self, fname, lname, address):
        super().__init__(fname, lname, address)  # corrected syntax

# Creating objects with correct parameters
x = B("Prami", "Olsen", "123 Main St")  # added missing address
y = C("John", "Doe", "456 Oak Ave")     # corrected parameters

x.printname()
y.printaddress()  # will print the address
"""
class A:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class B(A):
    def __init__(self, fname, lname, address):
        A.__init__(self, fname, lname)  # Initialize parent class
        self.address = address  # Add the new address attribute

    def printaddress(self):
        print(self.address)

class C(B):
    def __init__(self, fname, lname, address):
        B.__init__(self, fname, lname, address)  # Initialize parent class

# Create objects with all required parameters
x = B("Prami", "Olsen", "123 Main Street")
y = C("John", "Doe" ,"456 Oak Avenue")

x.printname()       # Prints: Prami Olsen
x.printaddress()    # Prints: 123 Main Street
y.printname()       # Prints: John Doe
y.printaddress()    # Prints: 456 Oak Avenue








