a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = input("Give mathematical operation as above")
if(c == "+"):
    print(a + b)
elif(c == "-"):
    print(a - b)
elif(c == "*"):
    print(a * b)
elif(c == "/"):
    if(b == 0):
        print("Undefine")
    else:
        print(a / b)
else:
    print("no operation found")