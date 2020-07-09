import sys

sys.path.append("C:/Users/shaik/PycharmProjects/pythonBasics/pack1")
sys.path.append("C:/Users/shaik/PycharmProjects/pythonBasics/pack1/pack1sub1")
sys.path.append("C:/Users/shaik/PycharmProjects/pythonBasics/pack2")

from emp import Employee
e=Employee(101,"scott",40000)
e.displayemp()
import stu
stu.display()

import pack2.stu    #since there are 2 stu modules in different packages,we need to specify package name for differenciate
s=pack2.stu.Student(101,"abc","A")
s.displaystu()