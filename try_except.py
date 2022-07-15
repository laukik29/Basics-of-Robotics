try:
    ans = 10/0
    num = input("enter a number ")
    print(num)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid input")