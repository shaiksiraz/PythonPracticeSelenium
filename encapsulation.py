class A:
    __pvar=100
    def m1(self):
        print("example of private variable",self.__pvar)

obja=A()
obja.m1()

#print("obja.__pvar") #private variable cannot be accessed from ouside the class


class B:
    def __pmethod(self):
        print("This is private methods for class B")
    def m(self):
        print(" this is m method of class B")
        print("calling private method within the class")
        self.__pmethod()
obja=B()
obja.m()


class C:
    __empid=100

    def setempid(self,empid):
        self.__empid=empid
        print("empid value is set successfully as :",empid)

    def getempid(self):
        print("empid value is :",self.__empid)

print("*** accessing private variable outside the class")
obja=C()
obja.getempid()
obja.setempid(102)
obja.getempid()
