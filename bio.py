class A:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class B(A):
    def __init__(self, fname, lname, address):
        A.__init__(self, fname, lname)  
        self.address = address

    def printaddress(self):
        print(self.address)

class C(B):
    def __init__(self, fname, lname, address):
        B.__init__(self, fname, lname, address)  


x = B("Prami", "Olsen", "Kathmandu")

x.printname()        
x.printaddress()