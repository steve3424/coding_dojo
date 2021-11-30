#Mutable:
#    if swap:
#        if instance:
#            new ref
#            is now local
#            can swap back to class ref to become global
#        elif class:
#            changing global ref
#            all instances reflect new ref
#    elif mod:
#        every change is global
#
#Immutable:
#    if swap:
#        if instance:
#            new ref
#            now local
#            CANT swap back to global
#        elif class:
#            changing global ref
#            all changes global
#    elif mod:
#        immutable
#        mod is really a swap

class Test:
    im = "string"
    def __init__(self):
        pass

t1 = Test()
t2 = Test()
print(Test.im)
print(t1.im)
print(t2.im)
print('\n')

t1.im = "hey"
print(Test.im)
print(t1.im)
print(t2.im)
print('\n')

Test.im = "change"
print(Test.im)
print(t1.im)
print(t2.im)
print('\n')

t1.im = Test.im
print(Test.im)
print(t1.im)
print(t2.im)
print('\n')

Test.im = "final change"
print(Test.im)
print(t1.im)
print(t2.im)
print('\n')
