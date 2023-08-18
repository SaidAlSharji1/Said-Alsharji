import numpy as np
die=[1,2,3,4,5,6]
x1=np.random.choice(die)
x2=np.random.choice(die)
if x1 + x2 <6:
    print("Turn is not good")
elif x1 + x2 > 6 :
    print("Turn is good")

    
    