"""print("hello Anil Kumar")
print("Good Morning\ni have assigned a work to you")
print("\nsome block of code.....\n")
print("hello Anil Kumar")
print("Good Morning")
print("\nnew block of code...\n")
print("hello Anil Kumar")
print("Good Morning")"""

'''def sayHello():
    print("hello Anil kumar")
    print("Good Morning")

sayHello()
print("some block of code...")
sayHello()
print("New block of code...")
sayHello()'''

"""def sayHello(name='user'):
    print("hello",name)
    print("Good Morning")
sayHello("Anil kumar")
print("\nsome block of code...\n")
sayHello("Krishna")
sayHello()"""

'''def sayHello(name='user'):
    print("hello",name)
    print("Good Morning")
def add(fn,sn):
    result = fn+sn
    print('Result',result)
sayHello("Anil kumar")
add(25,31)'''
"""def sayHello(name='user'):
    print("hello",name)
    print("Good Morning")
def add(fn,sn):
    result = fn+sn
    print('Result'+str(result))
sayHello("Anil kumar")
add(25,31)
add(99,85)
sayHello()
add(67,78)"""

'''def sayHello(name='user'):
    print("hello",name)
    print("Good Morning")
def add(fn,sn):
    result = fn+sn
    print('Result'+str(result))
def getSum(*x):
    result=0
    for a in x:
        result+=a
    print("Result",result)
    print(x[1])
sayHello("Anil kumar")
getSum(25,31,45,13,36)
add(11,21)'''

"""def sayHello(name,age):
    print("hello:",name)
    print("Good Morning")
    print("Age:",age)
#sayHello("Dommala krishna",55)
sayHello(age=55,name="Dommala krishna")"""

def sayHello(name,age,country="India"):
    print("hello:",name)
    print("Age:",age)
    print("I am from",country)
sayHello("krishna",55)
sayHello("Anil",32,"Russia")
