#EJERCICIO2

import random
import math
A=[]
N=1000
for i in range (N):
  val = random.randint (0, 255)
  A.append(val)
e=0
B=[]
for i in range (N):
    val2= A[e] **2
    e=e+1
    B.append(val2)
print ("Voltaje RMS para CC: ",math.sqrt((1/N)*(sum(B))))