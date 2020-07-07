class Parent():
    name="shaik"


class Child(Parent):
    name = "siraj"

print("if variable overriding in another class")
obj=Child()
print(obj.name)

print("if variable not overriding")
class Parent():
    name="shaik"


class Child(Parent):
    pass

obj=Child()
print(obj.name)

print("methods overriding")
class Bank():
    def rateofinterest(self):
        print("interest rate is 6%")



class ICICI(Bank):
    def rateofinterest(self):
        print("interest rate is %8")

obj=ICICI()
obj.rateofinterest()

del obj

print("Overload methods")


class Meeting():
    def welcomemessage(self,name=None):
        if name==None:
            print("Hello there!!")
        else:
            print("Hello ",name)

obj=Meeting()
obj.welcomemessage()


class Greetings():
    def welcomemessage(self):
        print("Hello there!!")


class Meeting(Greetings):
    def welcomemessage(self,name=None):
        if name==None:
            super().welcomemessage()
        else:
            print("Hello ",name)

obj=Meeting()
obj.welcomemessage()
obj.welcomemessage("Siraj")




