import numpy as np
l1=[9,7,100,6,8,7]
print(l1,"\n")
avg = np.average(l1)
print("Avrage = ", avg,"\n")
std= np.std(l1)
print("standard deviation = ",std,"\n")

for i in l1:
    z= (i-avg)/std
    print(z," of ",i)
    
s1=set(l1)
l1=list(s1)

print(s1)
print(l1)
print(type(l1))


l1=[58,94,26,46,47,3,5,47,50,43]
minl=min(l1)
maxl=max(l1)
print(maxl)
for i in l1:
    x = (i - minl)/ (maxl-minl)
    print("normalize of ",i,"= ",x)
