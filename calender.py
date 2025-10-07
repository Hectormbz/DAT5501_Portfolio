import sys
numDays = int(input("How many days in the month"))
firstDay = int(input("What day does it start on: enter 1 for sunday, 2 for monday etc..."))
print("S   M   T   W   T   F   S\n")
for i in range(firstDay - 1):
    print("-- ", end = ' ')
for a in range(8 - firstDay):
    print(a+1," ", end = ' ')
b = 8 - firstDay
while b < numDays:
    print("\n")
    for c in range(7):
        if b == numDays:
            sys.exit()
        b = b + 1
        print(b, " ", end = ' ')