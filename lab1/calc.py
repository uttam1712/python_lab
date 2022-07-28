n1 = int(input("Enter number 1 : "))
n2 = int(input("Enter number 2 : "))
op = input("Enter operator : ")

if op == "+":
    print("Sum =", n1+n2)
elif op == "-":
    print("Diff =", n1-n2)
elif op == "*":
    print("Multiplication =", n1*n2)
elif op == "/":
    print("Division =", n1/n2)
elif op == "%": 
    print("Modulo =", n1%n2)
else:
    print("Invalid operator")
