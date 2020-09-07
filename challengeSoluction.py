# 1 - Desafio Lógico - Ao receber uma matriz quadrada, retorne a diferença entre a soma de suas diagonais

def sumDiagonals(matrix, right = 0):
  # matriz quadrada (n * n) tem tamanho iguais na sua largura e profundidade 
  size = len(matrix[0])
  sum = 0

  # soma sua diagonal
  for index in range(0, size):
    if right: # se for a diagonal da direta o calculo muda
      sum += matrix[index][(size - 1) - index]
    else: # caso contrario
      sum += matrix[index][index]

  return sum

# Exemplo

# calcula a diferença
def diffDiagonals(matrix):
  right = 1
  return sumDiagonals(matrix) - sumDiagonals(matrix, right) 

a = [[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 8], [1, 2, 3, 8]]

print(diffDiagonals(a))