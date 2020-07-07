try:
    print(" Reached try block")
    #print(50/0)

except ZeroDivisionError:
    print("reached ZeroDivisionError exception")
else:
    print("Reached else part as no exceptions raised")
finally:
    print("Reached finally block")
try:
    s=None
    print(len(s))
except TypeError:
    print("Reached TypeError exception")

def enterage(age):
    if age<0 :
        raise ValueError("only positive values should be entered!")
    elif age %2 == 0:
        print("value is even")
    else:
        print("value is odd")
print("Raising exceptions")
num=-5
try:
    enterage(num)
except ValueError:
    print("Please enter positive value")
except:
    print("something wrong")

print("capturing exception descriptions")
try:
    num=one
    print("number is ",num)
except NameError as ne:
    print("exception occured was : ",ne)