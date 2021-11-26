"""
Class attributes and their awful behavior
"""

## 2 fundamental concepts:
##     1. Class vs instance
##     2. Mutable vs immutable 
#
#class Person:
#    name = "Rob"
#
#    def __init__(self):
#        self.var = "something"
#
#####################################################################
#
## immutable example
#print("Blueprint: " + Person.name)
#
#p1 = Person()
#p2 = Person()
#
#print("P1: " + p1.name)
#print("P2: " + p2.name)
#print("\nChanging blueprint....\n")
#Person.name = "Sally"
#
#print("Blueprint: " + Person.name)
#print("P1: " + p1.name)
#print("P2: " + p2.name)
#
#print("\nChanging p1....\n")
#Person.name = "New"
#p1.name = "Rich"
#print("Blueprint: " + Person.name)
#print("P1: " + p1.name)
#print("P2: " + p2.name)

s = [1,2,3]

class L:
    def __init__(self, stuff):
        self.stuff = stuff

l1 = L(s)
l2 = L(s)

l1.stuff[0] = 99

print(l1.stuff)
print(l2.stuff)
