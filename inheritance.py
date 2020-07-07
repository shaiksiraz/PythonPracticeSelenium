class A:
    def m1(self):
        print("This is m1 method in class A")


class B(A):
    def m2(self):
        print("This is m2 from class B")
        super().m1()


obja=B()
obja.m2()


class C:
    ca,cb=1000,2000
    def m1(self):
        print("This is method1 from class C")


class D(C):
    a,b=100,200
    def m3(self):
        c,d=10,20
        print("This is m3 from the class C")
        print("printing local variables : ",c,d)
        print("Priting class variables :",self.a,self.b)
        print("priting parent class variables :",self.ca,self.cb)

objd=D()
objd.m3()

a,b =100000,200000


class A:
    a, b = 10000, 20000

    def m1(self):
        a,b=100,200
        print("This is m1 from class A")
        print("printing local variables:",a,b)


class B(A):
    a,b=10,20

    def m2(self):
        a,b=1,2
        print("This is m2 from class B")
        print("Printing local variable:",a,b)
        print("printing class variables: ",self.a,b)
        print("printing parent class variables:",super().a,super().b)
        print("printing global variables :",globals()['a'],globals()['b'])

obja=B()
obja.m2()

print("if both parent and child classes have constructors")
class A():
    def __init__(self):
        print("class A constructor invoked")


class B(A):
    def __init__(self):
        print("Class B constructor invoked")

obja=B()
del obja

print("if  parent classes has constructor, but not child class")


class A():
    def __init__(self):
        print("class A constructor invoked")


class B(A):
    def m1(self):
        print("")


obja=B()

print("Invoking parent class constructor along with child class constructor")


class A:
    def __init__(self):
        print("parent class constructor invoked")


class B(A):
    def __init__(self):
        print("child class constructor invoked")
        super().__init__()

obja=B()
