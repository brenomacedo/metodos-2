import methods.integration.newton_cotes as NC
import math

FUNCTIONS = {
  0: math.cos,
  1: math.sin,
  2: math.sqrt,
  3: math.exp
}

METHODS = {
  0: {
    0: NC.closed1stGrade,
    1: NC.closed2ndGrade,
    2: NC.closed3rdGrade,
    3: NC.closed4thGrade
  },
  1: {
    0: NC.opened1stGrade,
    1: NC.opened2ndGrade,
    2: NC.opened3rdGrade,
    3: NC.opened4thGrade
  }
}

def iterate(method, function, a, b, error):
  current_error = float('inf')
  partitions = 1

  prev_result = None
  result = None

  while current_error > error:
    prev_result = result
    result = 0

    h = (b - a) / partitions
    for i in range(partitions):
      result += method(function, a + h*i, a + h*(i + 1))

    if prev_result != None:
      current_error = abs(prev_result - result)

    partitions *= 2

  return result



def partitionate(method, function, a, b, numberOfPartitions):
  result = 0

  h = (b - a) / numberOfPartitions
  for i in range(numberOfPartitions):
    result += method(function, a + h*i, a + h*(i + 1))

  return result

def main():
  print('Escolha a função que você quer aproximar: ')
  print('0: cos')
  print('1: sin')
  print('2: sqrt')
  print('3: exp')

  func = 0
  getFunc = True
  while getFunc:
    try:
      func = int(input('Escolha uma opção: '))
      
      if func >= 0 and func <= 3:
        getFunc = False
    except:
      pass

  #=============================================

  a = 0
  b = 0

  getValues = True
  while getValues:
    try:
      a = float(input('Escolha o valor do x inicial: '))
      b = float(input('Escolha o valor do x final: '))
      
      if b > a:
        getValues = False
    except:
      pass

  #=============================================

  print('Escolha a filosofia: ')
  print('0: fechada')
  print('1: aberta')

  philosophy = 0
  getPhilosophy = True
  while getPhilosophy:
    try:
      philosophy = int(input('Escolha uma opção: '))
      
      if philosophy >= 0 and philosophy <= 1:
        getPhilosophy = False
    except:
      pass

  #=============================================

  print('Escolha o grau: ')
  print('0: grau 1')
  print('1: grau 2')
  print('2: grau 3')
  print('3: grau 4')

  grade = 0
  getGrade = True
  while getGrade:
    try:
      grade = int(input('Escolha uma opção: '))
      
      if grade >= 0 and grade <= 3:
        getGrade = False
    except:
      pass

  #=============================================

  print('Escolha o ponto de parada: ')
  print('0: Partição')
  print('1: Erro')

  stopPoint = 0
  getStopPoint = True
  while getStopPoint:
    try:
      stopPoint = int(input('Escolha uma opção: '))

      if stopPoint >= 0 and stopPoint <= 1:
        getStopPoint = False
    except:
      pass

  #=============================================

  if (stopPoint == 1):
    error = 0
    getError = True
    while getError:
      try:
        error = float(input('Escolha o erro: '))

        if error > 0.00000001:
          getError = False
      except:
        pass

    result = iterate(METHODS[philosophy][grade] ,FUNCTIONS[func], a, b, error)
    print(result)
  else:
    partitions = 0
    getPartitions = True
    while getPartitions:
      try:
        partitions = int(input('Escolha o número de partições: '))

        if partitions > 0:
          getPartitions = False
      except:
        pass

    result = partitionate(METHODS[philosophy][grade], FUNCTIONS[func], a, b, partitions)
    print(result)

if __name__ == '__main__':
  main()