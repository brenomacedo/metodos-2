from math import sqrt

GL_2PT_W = [1, 1]
GL_2PT_ALPHA = [-sqrt(1/3), sqrt(1/3)]
def gauss_legendre_2pts(function, a, b):
  x = lambda alpha_k : ((a + b) / 2) + ((b - a) / 2) * alpha_k

  summation = 0
  for i in range(2):
    summation += function(x(GL_2PT_ALPHA[i])) * GL_2PT_W[i]

  result = ((b - a) / 2) * summation
  return result

GL_3PT_W = [5/9, 8/9, 5/9]
GL_3PT_ALPHA = [-sqrt(3/5), 0, sqrt(3/5)]
def gauss_legendre_3pts(function, a, b):
  x = lambda alpha_k : ((a + b) / 2) + ((b - a) / 2) * alpha_k
  
  summation = 0
  for i in range(3):
    summation += function(x(GL_3PT_ALPHA[i])) * GL_3PT_W[i]

  result = ((b - a) / 2) * summation
  return result

GL_4PT_W = [0.347854845137454, 0.652145154862546, 0.652145154862546, 0.347854845137454]
GL_4PT_ALPHA = [
  -sqrt( (3/7) + ((2*sqrt(6/5)) / 7) ),
  -sqrt( (3/7) - ((2*sqrt(6/5)) / 7) ),
  sqrt( (3/7) - ((2*sqrt(6/5)) / 7) ),
  sqrt( (3/7) + ((2*sqrt(6/5)) / 7) )
]
def gauss_legendre_4pts(function, a, b):
  x = lambda alpha_k : ((a + b) / 2) + ((b - a) / 2) * alpha_k
  
  summation = 0
  for i in range(4):
    summation += function(x(GL_4PT_ALPHA[i])) * GL_4PT_W[i]

  result = ((b - a) / 2) * summation
  return result
