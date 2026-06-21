def add(a,b):
    return a + b
def multi(a,b):
    return a * b
def sub(a,b):
    return a - b
def div(a,b):
    return a / b

cont = 'y'

a = float(input("Enter a number "))
while cont == "y":
    function = input("select operator + , - , / , * ")
    b = float(input("Enter b number "))
    if(function == '+'):
        a = add(a,b)
    elif(function == "*"):
        a = multi(a,b)
    elif(function == '-'):
        a =sub(a,b)
    elif(function == '/'):
        a = div(a,b)

    print('current Result',a)
    cont = input("Do you want to continue y or n: ")
    if cont.lower() != "y":
        break