a=0.0
b=1
n=256
h=(b-a)/n
v= (( (a**2)-(2**6) )**(1/6)) + (( (b**2)-(b**6) )**(1/6))
for i in range(1,n):
   v += 2*  ( ((a+(i*h))**2)-((a+(i*h))**6) )**(1/6)
   print v     
t=(h/2.0)*v
f=2**0.5
print t
print h
