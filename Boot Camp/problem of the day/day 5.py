numerator=[1,2,2,8]
denomonator=[2,4,6,12]
i=0
while i<= (len(numerator)-1):
    x=(numerator[i]/denomonator[i])+(numerator[i+1]/denomonator[i+1])
    print(x)
    i+=2