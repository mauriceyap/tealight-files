a=0.0
b=1
n=2048
h=(b-a)/n
v= (( (a**2)-(a**6) )**(1/6.0)) + (( (b**2)-(b**6) )**(1/6.0))
for i in range(1,n):
   v += 2*  ( ((a+(i*h))**2)-((a+(i*h))**6) )**(1/6.0)
    
t=(h/2.0)*v
trap=t*4
print 'trap rule ='t
print trap