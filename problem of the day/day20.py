A = [2,4,6,8,9,10,12]
B = [2,4,6,8,10,12]

for i in range(len(A)) :
    if A[i] not in B:
        print(i)