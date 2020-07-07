print("*args in methods ")
def sum(*args):
    s=0
    for i in args:
       s+=i
    print("sum  is : ",s)

sum(1,2)

print("*args while calling methods")

def add(a,b,c):
    print(" arguments are :",a,b,c)

list=[1,3,2]
add(*list)

print("**keywordarguments example")
def keywordslist(**kwargs):
    for i,j in kwargs.items():
        print("key is :",i,"  value is : ",j)

keywordslist(name="abc",sport="xyz")

print("**kwargs while passing args")

def my_three(a,b,c):
    print(a,b,c)


a={'a':"one",'b':"two",'c':"three"}
my_three(**a)

