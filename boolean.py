def isOrdered(x, y, z):
    if x > y > z:
        print(x, y, z, "In Order :)")
        return True
    if x < y < z:
        print(x, y, z, "In Order :)")
        return True
    else:
        print(x, y, z, "NOT IN ORDER!!!!!!!")
        return False


while True:
    n1, n2, n3 = input("Enter three numbers in an order ").split()
    print(isOrdered(n1, n2, n3))
