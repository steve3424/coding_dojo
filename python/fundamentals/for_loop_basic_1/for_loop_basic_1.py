from menu import RunMenu, FuncObj

def Basic():
    print("Basic - Print all integers from 0 to 150.")
    for i in range(1, 151):
        print(i)

def MultiplesOfFive():
    print("Multiples of Five - Print all the multiples of 5 from 5 to 1,000")
    for i in range(5, 1001, 5):
        print(i)

def CountingDojoWay():
    print("Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print Coding instead. If divisible by 10, print Coding Dojo.");
    for i in range(1, 101):
        if i % 10 == 0:
            print("Coding Dojo")
        elif i % 5 == 0:
            print("Coding")
        else:
            print(i)

def WhoaSucker():
    print("Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.")
    res = 0
    for i in range(1, 500001, 2):
        res += i
    print(res)

def Countdown():
    print("Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.")
    for i in reversed(range(2, 2019, 4)):
        print(i)

def FlexibleCounter():
    print("Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)")
    print("Choose low num: ")
    low = int(input())
    print("Choose high num: ")
    high = int(input())
    print("Choose mult: ")
    mult = int(input())
    print("low:" + str(low))
    print("high:" + str(high))
    print("mult:" + str(mult))
    for i in range(low, high + 1):
        if i % mult == 0:
            print(i)

if __name__ == "__main__":
    functions = [FuncObj(Basic), FuncObj(MultiplesOfFive), FuncObj(CountingDojoWay), FuncObj(WhoaSucker), FuncObj(Countdown), FuncObj(FlexibleCounter)]
    func_to_run = functions[RunMenu("Choose a function below", functions)]
    func_to_run.func()