o=[7,5,2,0,1,8]
f=[6,5,0,-1,0,7]
x=0
for i in range(len(o)):
    x+=((f[i]-o[i])**2)
    print(x)
t=x/(len(o))
print(t)