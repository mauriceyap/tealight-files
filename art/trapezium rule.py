a=0
b=0.5
n=5
h=(b-a)/n
c=((1+a^3)^0.5)
d=((1+b^3)^0.5)
for i in range(1,n):
   e = 2*((1+(a+(i*h))^3)^0.5)
t=(h/2)*(c+d+e)
print t
print c
print d