import math

def newtonraphson(function, derivative, x, tolerance=0.00001, maxIterations=1000):
  for i in range(maxIterations):
    xNew = x - function(x)/derivative(x)
    if abs(xNew - x) < tolerance:
      break
    x = xNew
  return i, xNew
  
y = lambda x: x * math.log10(x) - 1.3
y_prime = lambda x: math.log10(x) + math.log10(math.e)

iterations, x = newtonraphson(y, y_prime, 1)
print("after %i iterations the root is %g" % (iterations, x))