class A:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class B(A):
    def __init__(self, fname, lname, address):
        A.__init__(self, fname, lname)  # Direct call to parent class
        self.address = address

    def printaddress(self):
        print(self.address)


class C(B):
    def __init__(self, fname, lname, address):
        B.__init__(self, fname, lname, address)  # Direct call to parent class




class D(C):
    def __init__(self, fname, lname, address, age):
        C.__init__(self, fname, lname, address)  # Only pass 3 parameters
        self.age = age

    def printage(self):
        print(self.age)


class E(D):
    def __init__(self, fname, lname, address, age):
        D.__init__(self, fname, lname, address, age)

class F(E):
    def __init__(self, fname, lname, address, age, university):
        E.__init__(self,fname,lname,address,age)
        self.university=university
    def printuniversity(self):
        print(self.university)

class G(F):
    def __init__(self,fname,lname,address,age,university):
        F.__init__(self,fname,lname,address,age,university)

class H(G):
    def __init__(self,fname,lname,address,age,university,experience):
        G.__init__(self,fname,lname,address,age,university)
        self.experience=experience
    def printexperience(self):
        print(self.experience)
class I(H):
    def __init__(self,fname,lname,address,age,university,experience):
        H.__init__(self,fname,lname,address,age,university,experience)


# Example usage
x = I("Prami", "Olsen", "Kathmandu", 25,"Tribhuvan University","Nothing")  # Using numeric age
x.printname()
x.printaddress()
x.printage()
x.printuniversity()
x.printexperience()