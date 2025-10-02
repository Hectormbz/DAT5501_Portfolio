import math
def CIC(savings, rate, years):
    rate = 1 + rate/100
    for i in range(years):
        savings = savings * rate
        print(savings)
    print(math.log(2, rate))
CIC(100, 5, 8)
