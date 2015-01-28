#Trapezium rule
def trapRule(a,b,n):
  h=(b-a)/n
  v= (( (a**2)-(a**6) )**(1/6.0)) + (( (b**2)-(b**6) )**(1/6.0))
  u=0
  for i in range(1,n):
     u=(a+(i*h))
     v += 2*  ( (u**2)-(u**6) )**(1/6.0)
        
  t=(h/2.0)*v
  return t*4

  
#Mid ordinate rule  
def midOrdRule(a,b,n):
  h=(b-a)/n
  v=0.0
  u=0
  for i in range(1,n-1):
    u=(a+ (((2.0*i)-1.0)*h) /2.0)
    v += (( (u**2)-(u**6) )**(1/6.0))
  return v*h*4

#Output
for x in xrange(6):
  print 'M',(2**x),'=',midOrdRule(0.0,1,(2**x))
  print 'T',(2**x),'=',trapRule(0.0,1,(2**x))
    
 
 