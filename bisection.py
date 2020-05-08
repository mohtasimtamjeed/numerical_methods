import math

def value(x):
  #print("blah",(x * math.exp(x)) - math.cos(x))
  return ((x * math.exp(x)) - math.cos(x))

#def maxIterations

def bisection(interval, decimals):
  n = (decimals * math.log(10) + math.log(abs(interval[1] - interval[0])))/math.log(2)

  n = math.ceil(n)

  a, b = interval[0], interval[1]

  

  for x in range(0, n):
    Fa = value(a)
    Fb = value(b)
    
    r = (a + b)/2
    
    Fr = value(r)

    if Fr == 0:
      print(r, Fr)
      return(r, Fr)

    else:
      if Fa * Fr < 0:
        #Fb = Fr
        b = r
      else:
        #Fa = Fr
        a = r

  print(r, Fr)

bisection([0,1],  4)