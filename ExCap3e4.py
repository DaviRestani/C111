import numpy as np

#Exercicio 1
print("------------------------Exercício 1------------------------")
arr = np.linspace(0, 1, 21)
print('Primeiro array:',arr)

#Exercício 2
print("------------------------Exercício 2------------------------")
arr1 = np.arange(0, 51, 2)
arr2 = np.arange(100, 50, -2)
print("Array 1: ",arr1)
print("Array2: ",arr2)
conc = np.concatenate((arr1,arr2))
print("Array Concatenado:",conc)

#Exercicio 3
print("------------------------Exercício 3------------------------")
arr3 = np.flip(conc)
print("Array decrescente:",arr3)

#Exercício 4
print("------------------------Exercício 4------------------------")
matriz = np.arange(1,13).reshape(3,4)
print("Matriz:",matriz)
matriz2 = matriz.reshape(12,)
print("Array da matriz:",matriz2)


#Exercicio 5
print("------------------------Exercício 5------------------------")
matriz3 = np.arange(10,22).reshape(3,4)
print('Matriz:', matriz3)
numero_linhas = matriz3.shape[0]
numero_colunas = matriz3.shape[1]
print("Numero de linhas:",numero_linhas)
print("Numero de colunas:",numero_colunas)

mult = numero_linhas * numero_colunas

if mult % 2 == 0:
    print("Esse array possui um número par de elementos")
else:
    print("Esse array possui um número impar de elementos")



