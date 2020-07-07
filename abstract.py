from abc import ABC,abstractmethod
class A(ABC):

    @abstractmethod
    def abstractmethod(self):
        None


class B(A):
    def abstractmethod(self):
        print("abstract method implemented")

obja=B()
obja.abstractmethod()
#objb=A() # we cannot create object for abstract class as few or all the methods are unimplemented

class Animal(ABC):
    def __init__(self):
        print("Abstract class constructor")
    @abstractmethod
    def eat(self):
        None

class Lion(Animal):
    def eat(self):
        print(" Lion eat non veg")

class Goat(Animal):
    def legs(self):
        print("has 4 legs")

    def eat(self):
        print("Goat eats veg")

ani_lion=Lion()
ani_lion.eat()
ani_goat=Goat()
ani_goat.eat()

#ani=Animal()
#ani.eat() #object cannot be created for abstract class

class A(ABC):
    @abstractmethod
    def m1(self):
        None

    @abstractmethod
    def m2(self):
        None

class B(A):

    def m1(self):
        print("m1 implemented in class B")

#objb=B() #cannot create object as all the abstract methods were not implementedc

class C(B):

    def m2(self):
        print("m2 method implemented in class C")

obj=C()
obj.m1()
obj.m2()

class cal(ABC):
    def __init__(self,value):
        self.value=value

    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def sub(self):
        pass

class B(cal):

    def add(self):
        print("add value is ",self.value+100)

    def sub(self):
        print(" sub value is ",self.value-10)

print("constructer in abstraction classes")
obj=B(100)
obj.add()
obj.sub()