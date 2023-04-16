def closed1stGrade(function, a, b):
  f0 = function(a)
  f1 = function(b)
  result = ((b - a) / 2) * (f0 + f1)
  return result

def closed2ndGrade(function, a, b):
  deltaX = (b - a)
  h = deltaX / 2

  f0 = function(a)
  f1 = function(a + h)
  f2 = function(b)

  result = (deltaX / 6) * (f0 + 4*f1 + f2)
  return result

def closed3rdGrade(function, a, b):
  deltaX = (b - a)
  h = deltaX / 3

  f0 = function(a)
  f1 = function(a + h)
  f2 = function(a + 2*h)
  f3 = function(b)

  result = (deltaX / 8) * (f0 + 3*f1 + 3*f2 + f3)
  return result

def closed4thGrade(function, a, b):
  deltaX = (b - a)
  h = deltaX / 4

  f0 = function(a)
  f1 = function(a + h)
  f2 = function(a + 2*h)
  f3 = function(a + 3*h)
  f4 = function(b)

  result = (deltaX / 90) * (7*f0 + 32*f1 + 12*f2 + 32*f3 + 7*f4)
  return result

def opened1stGrade(function, a, b):
  deltaX = (b - a)
  h = deltaX / 3

  f0 = function(a + h)
  f1 = function(a + 2*h)

  result = (deltaX / 2) * (f0 + f1)
  return result

def opened2ndGrade(function, a, b):
  deltaX = (b - a)
  h = deltaX / 4

  f0 = function(a + h)
  f1 = function(a + 2*h)
  f2 = function(a + 3*h)

  result = (deltaX / 3) * (2*f0 - f1 + 2*f2)
  return result

def opened3rdGrade(function, a, b):
  deltaX = (b - a)
  h = deltaX / 5

  f0 = function(a + h)
  f1 = function(a + 2*h)
  f2 = function(a + 3*h)
  f3 = function(a + 4*h)

  result = (deltaX / 24) * (11*f0 + f1 + f2 + 11*f3)
  return result

def opened4thGrade(function, a, b):
  deltaX = (b - a)
  h = deltaX / 6

  f0 = function(a + h)
  f1 = function(a + 2*h)
  f2 = function(a + 3*h)
  f3 = function(a + 4*h)
  f4 = function(a + 5*h)

  result = (deltaX / 20) * (11*f0 - 14*f1 + 26*f2 - 14*f3 + 11*f4)
  return result
