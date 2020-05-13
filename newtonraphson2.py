import math

def newtonraphson(function, derivative, x, tolerance=0.00001, maxIterations=1000):
  for i in range(maxIterations):
    xNew = x - function(x)/derivative(x)
    if abs(xNew - x) < tolerance:
      break
    x = xNew
  return i, xNew

y = lambda x: x * math.sqrt(15) - 1
y_prime = lambda x: math.sqrt(15)

iterations, x = newtonraphson(y, y_prime, 1, 0.0001)
print("after %i iterations the root is %g" % (iterations, x))