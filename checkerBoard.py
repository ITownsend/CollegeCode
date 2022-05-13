
n = int(input("Enter a number "))

#for i in range(n):
#   print('*', end=' ')
#print("")
#for j in range(n):
#    print(' *', end='')

# n is the number of rows
#range(start, stop, interval)

#outer loop
for row in range(1,n+1):
    #nested loop
    for col in range(n):
        #display pattern (star)
        if col == 0 and (row % 2 == 0):
            #print('row = ', row)
            #print('col = ', col)
            print(" *", end='')
        else:
            print("*", end='')

    # new line after each row
    print('\r')