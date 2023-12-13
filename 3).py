#EJERCICIO3

import random
import math

P=int(input("Ingrese el valor del voltaje pico[V]: "))
A=[]
N=1000
for i in range (N):
  val = random.randint (-P, P)
  A.append(val)
e=0
B=[]
for i in range (N):
    val2= A[e] **2
    e=e+1
    B.append(val2)
print ("Metodo1 Voltaje RMS para AC: ",math.sqrt((1/N)*(sum(B))))

print ("Metodo2 Voltaje RMS para AC: ",P/math.sqrt(2))