#Basic def practice:
def funct():
    print("welcome to the world of python")

funct()

#evenOdd:

def evenOdd(x):
    if x%2==0:
         return "Even"
    else:
        return odd
      

print(evenOdd(14))
print(evenOdd(7))

# Arbitrary Keyword  Arguments

def myFun(*argv):
    for arg in argv:
        print(arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

