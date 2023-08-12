l1=[]
for i in range(5):
    n=int(input("Enter any number to add: "))
    l1.append(n)
g=5
for i in range (len(l1)):
    for j in range(len(l1)):
        if l1[i] == l1[j]:
            continue
        elif l1[i] + l1[j] == g:
            print (l1[i] ,l1[j])
        