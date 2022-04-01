# AULA 2 - NUMPY
import numpy as np

# LIDAR COM NÚMEROS ALEATÓRIOS
# subpacote random do numpy
# semente de dados

# rand - geração de números float
#arr = np.random.rand(6)
# broadcasting - a possibilidade de operações entre escalares e vetores
#print(arr * 100)

# randint - geração de números inteiros
#arr2 = np.random.randint(1,100,10)
#print(arr2)

# EXTRAINDO ELEMENTOS ÚNICOS DE UMA COLEÇÃO
np.random.seed(10)
arr = np.random.randint(1,10,10)
#print(arr)
#print(np.unique(arr,return_counts=True))

# OPERAÇÕES COM COLEÇÕES NO PYTHON
arr = np.arange(1, 5, 1)
arr2 = np.arange(5, 9, 1)
#print(arr)
#print(arr2)
#print(arr * arr2)

# CRIANDO UM ARRAY 2-D

mtz = np.arange(9).reshape(3, 3)
print(mtz)
print(mtz.sum(axis=0))
print(mtz.mean(axis=1).astype(int))
