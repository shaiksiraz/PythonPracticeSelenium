

# different python files are called modules and can be called with import statement
# approach 1
import Operations

Operations.add(10, 20)
Operations.sub(10, 6)

# approach 2
from Operations import add, sub

add(10, 200)
sub(100, 50) \
 \
# approach 3
from Operations import *

add(29, 10)
sub(500, 100)

# Approach 1
import Animals, Birds

Animals.fly()
Birds.fly()

# Approach 2


from Birds import fly
from Animals import fly

fly()  # last imported module will be taken

from Birds import color, fly

color()
fly()
from Animals import color, fly

color()
fly()



# Approach 1 for accessig different moudle classes

import classA
import classB

obj2 = classB.B()
#obj2.m1()
obj1 = classA.A()
#obj1.m1()


#Approach 2 for accessing same name methods from different modules
from classA import A
from classB import B

obj1=A().m1()
obj2=B().m1()