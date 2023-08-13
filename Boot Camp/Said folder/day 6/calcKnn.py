import math
c=[7,7,3,1,3]
w=[70,40,40,40,70]
h=["bad","bad","Good","Good","bad"]
nc=int(input("Enter the cigarettes: "))
nw=int(input("Enter the weight: "))
nl=[]

for i in range(len(c)):
    d = math.sqrt((nc - c[i])**2 + (nw - w[i])**2)
    nl.append(d)


min(nl)
r = nl.index(min(nl))

print("The result is  ", h[r])
