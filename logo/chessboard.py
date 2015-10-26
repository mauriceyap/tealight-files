#Input variables
p=int(eval(input('Number of n values in approximations')))
a=float(eval(input('Lower bound')))
b=float(eval(input('Upper bound')))

#Trapezium rule
def trap(a,b,n):
  h=(b-a)/n
  v=(((a**2)-(a**6))**(1/6.0))+(((b**2)-(b**6))**(1/6.0))
  u=0
  for i in range(1,n):
     u=(a+(i*h))
     v+=2*((u**2)-(u**6))**(1/6.0)
  t=(h/2.0)*v
  return t

#Mid ordinate rule  
def midOrd(a,b,n):
  h=(b-a)/n
  v=0.0
  u=0
  for i in range(1,n+1):
    u=(a+(((2.0*i)-1.0)*h)/2.0)
    v+=(((u**2)-(u**6))**(1/6.0))
  m=v*h
  return m

#Output
print('Trapezium rule approximations:')
for x in range(p):
  print('T',(2**x),'=',trap(a,b,(2**x)))

print('Midpoint rules approximations:')
for x in range(p):
  print('M',(2**x),'=',midOrd(a,b,(2**x)))

print('Simpsons rules approximations:')
for x in range(p):
  print('S',(2**x),'=',((2*(midOrd(a,b,(2**x)))+(trap(a,b,(2**x))))/3))
