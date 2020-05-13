import math

def secant(function, x1, x2, tolerance=0.001, maxIterations=1000):
  for i in range(maxIterations):
    xNew = x2 - function(x2) * (x2 - x1)/(function(x2) - function(x1))
    if abs(xNew - x2) < tolerance:
      break
    else:
      x1 = x2
      x2 = xNew
  else:
    print("maximum iterations completed, tolerance not reached")

  return(i, xNew)

y = lambda x: x**3 - 2*x - 5
x1 = float(input("Enter first value of x:"))
x2 = float(input("Enter second value of x:"))

i, x = secant(y, x1, x2)
print("With x1=%a and x2=%a, Root is %f with %d iterations"%(x1, x2, x, i))
