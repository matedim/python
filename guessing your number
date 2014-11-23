import math
import random
count=input("Enter the range of guessing, ")
count=int(count)
next=count
otvet=0
i=1
step=0
print("this number is ", count,"?")
while otvet!=3:
    try:
        otvet=int(input("If more then Press 1, if less than Press 2, if guessing Press 3 "))
        if otvet==1:
        #count=count*2
            count=random.randint(count,next-1)
        elif otvet==2:
            count=random.randint(step,count)
            step+=1
            next-=1
        else:continue
        print("Hmmm .... this number is", int(count),"?")
        i+=1
    except:
        print("Make the right choice")
        continue
print('I m guessing your number for',i,'attempts! :-)' )
