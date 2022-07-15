from xml.dom.minidom import Element


num1 = float(input("enter the first no"))
op = input("enter the operator")
num2 = float(input("enter the second number"))

if op == '+' :
    print(num1+ num2)
elif op == '-':
    print(num1-num2)
else:
    print("invalid operation")
