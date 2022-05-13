def multiNum(a, b):
    product = 0
    while a > 0:
        if a % 2 != 0:
            product = product + b
        a = a // 2
        b = b * 2

    return product

    return c


num1, num2 = input("Enter 2 numbers ").split()
num1 = int(num1)
num2 = int(num2)
print("The Russian peasant Mulit Algorithm", num1, "*", num2, "=", multiNum(num1, num2))
