def colorConversion(red, green, blue):
    white = (red / 255, green / 255, blue / 255)
    cyan = (white - red / 255) / white
    magenta = (white - green / 255) / white
    magenta = int(magenta)
    yellow = (white - blue / 255) / white
    yellow = int(yellow)
    black = (1 - white)

    print("cyan =", cyan)
    print("white =", white)
    print("magenta =", magenta)
    print("yellow =", yellow)
    print("black =", black)


num1, num2, num3 = input("Enter your RGB scale number ").split()
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
# if input < 255:
# print("Number is too big")
# else:
print("Your RGB scale numbers converted to CMYK scale is", colorConversion(num1, num2, num3))
