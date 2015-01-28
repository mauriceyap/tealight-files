import math

a=0.0
b=1
n=10
h=(b-a)/n
v= (( (a**2)-(a**6) )**(1/6)) + (( (b**2)-(b**6) )**(1/6))
for i in range(1,n):
   v += 2*  ( ((a+(i*h))**2)-((a+(i*h))**6) )**(1/6)
    
half=(h/2.0)

t=half*v
f=2**0.5

x=math.pow(27,1/3)
print x
