import numpy as np

x = np.array([16,17,4,3,5,2])

def lNumber(nums):
    maxn= nums[-1]
    lList=[maxn]
    
    for i in range (len(nums)-2, -1,-1):
        print(nums[i])
        if nums[i] >= maxn:
            lList.append(nums[i])
            maxn = nums[i]
    lList.reverse()
    return lList


print(lNumber(x))