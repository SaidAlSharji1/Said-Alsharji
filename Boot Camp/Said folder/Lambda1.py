def square(a):
    return a * a
result = square(5)
print(result)

f= lambda a: a * a
result2 = f(5)
print(result)
# 
# def myFunc(n):
#     return a : a * n
# mydoubler = myFunc(5)
# print(mydoubler(2))

def oddEven(n):
    if n%2 == 0:
        return 'Even'
    else:
        return 'ood'
print(oddEven(10))
print(oddEven(9))


oddEven2 =lambda n:(n%2 and  'odd' or 'even')

print(oddEven2(5))
print(oddEven2(6))


# lengthOrigin = (lambda x=1, y=1


addition = lambda * args : sum (args) # many argument and we dont know how many
print(addition(10,20,3,51)) 