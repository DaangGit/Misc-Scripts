import random
import math
#Hello
#Estimating Pi

while True:
    k = input("Method? (1/2)\n")
    if  k == "1":

#Consider a unit circle and a square around it
#Area of circle = pi
#Area of Square = 4
#Probability of a random point being inside the circle = pi/4
#Thus, probability*4 = pi

        n = int(input("Number of Trials: ")) 
        s = 0
        for i in range(n+1):
            x = 1-(2*random.random())
            y = 1-(2*random.random())
            if x**2+y**2 <=1:
                s+=1
            if i%10000 == 0:
                print(i,"trials done.")
        print("Circle - Square Pi Estimate:",(s/n)*4)
        if input("Again? (y/n)\n")=="y":
            continue
        else:
            break

    elif k == "2":

#Buffon's needle problem
#Consider two lines 2 units apart and a needle 1 unit long
#Probability of that needle touching one of those lines = 1/pi
#https://en.wikipedia.org/wiki/Buffon%27s_needle_problem
#Monte Carlo Method to estimate pi

        n = int(input("Number of Trials: ")) 
        s = 0

        for i in range(n+1):
            x1 = (2*random.random())
            y1 = (2*random.random())
            angle = random.randint(-180,180)
            x2 = x1 + math.cos(math.radians(angle))  
            y2 = y1 + math.sin(math.radians(angle))
            if y2>=2 or y2<=0:
                s+=1
            if i%10000 == 0:
                print(i,"trials done.")
        print("Buffon's Needle Problem Pi Estimate:",(n/s))
        if input("Again? (y/n)\n")=="y":
            continue
        else:
            break