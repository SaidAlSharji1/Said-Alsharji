import re
def is_Even(L):
    evenList = []
    for num in L :
        if num % 2 == 0:
            evenList.append(num)
    return evenList
numbers= [10,2,3,14,17,29,19,18,22,26]
evens = is_Even(numbers)
print("Numbers: ",numbers)
print("Even Number: ", evens)

#Using filter
evensUsingfilter = list(filter(lambda n: n%2==0 , numbers))
print("evensUsingfilter",evensUsingfilter)

mapresult = list(map(lambda e : e*2,evensUsingfilter))
print(mapresult)
            


a=["dog", "cat", "wildcat", "thundercat", "cow", "hooo"]

r= re.compile(".*cat")
newlist = list(filter(r.match,a))
print(newlist)


newlist2 = list(filter(lambda animal : re.match(".*cat",animal),a))
length = list(map(lambda a: len(a) ,newlist)) #lenght of the world
print(newlist2)
print(length)


from functools import reduce  #reduce it will add all two element to gether until we get the sum  
emp = ['ali', 'ahmed', 'said', 'hamed']
hoursWorked=[1,3,5,7] # hours of each employe 
payPerHour=[2,4,6,8] # how much pear hour 
result5 = list(map(lambda hours , pay :  hours * pay , hoursWorked , payPerHour))
doblePay = list(map(lambda pay: pay * 2 , payPerHour))
print(doblePay)
print(result5 )
result5 = list(map(lambda hours , pay :  hours * pay , hoursWorked , doblePay))
print(result5 )
totalPayment = reduce (lambda a, b: a+b, result5)
print("Total",totalPayment)
print("----------")
total=0
for i in result5:
    total+= i
print("T= ", total) 
