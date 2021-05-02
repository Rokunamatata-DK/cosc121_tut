d_ = {'+':lambda x,y:x+y, "x":lambda x,y: x*y, "-":lambda x,y:x-y, "/":lambda x,y:x/y, "x^y":lambda x,y:x**y}



import random as rn
i=0
for i in range(0,5):

    print(rn.randint(0,9))
    i+=1