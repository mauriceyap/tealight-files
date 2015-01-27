a=0.5
b=0
n=5
h=(b-a)/n
t=((1+a^3)^0.5)+((1+b^3)^0.5)
for i in range(0,n):
   t += 2*((1+(a+(i*h))^3)^0.5)
s(h/2)*t
print s