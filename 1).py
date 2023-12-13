#EJERCICIO1
import random

A=[]
N=1000
for i in range (N):
  val = random.randint (0, 255)
  A.append(val)

A.sort()
vmin=A[0]
vmax=A[-1]
print ("Valor minimo de tension [V]: ",vmin)
print ("Valor maximo de tension [V]: ",vmax)
print ("Promedio de valores de tension [V]: ",(sum(A))/N)