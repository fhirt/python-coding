from mypackage import module1 as m1, module2 as m2
from mypackage.mysubpackage.module3 import people

from mypackage.helpers import math, string

m1.greet("Pythonista")
m2.depart("Pythonista")

for person in people:
    m1.greet(person)
    
    
print(string.shout(f"the area of a 5-by-8 rectangle is {math.area(5,8)}"))
