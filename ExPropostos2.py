import numpy as np

print("---------Exercicios propostos 2---------")

#Definindo a seed
#np.random.seed(5)

#Exercicio 1
print("------------------------Exercicio 1------------------------")
arr1 = np.random.randn(10)
print("Array 1:",arr1)
arr2 = arr1 * 100
print("Array 2:",arr2)
arr3 = arr2.astype(int)
print("Array 3:",arr3)

#Exercicio 2
print("------------------------Exercicio 2------------------------")
np.random.seed(10)
matriz = np.random.randint(1,50,(4,4))
print("Matriz:",matriz)

#Exercicio 3
print("------------------------Exercicio 3------------------------")

print("Media das linhas")
print("Linha 1:",matriz.mean(axis=0)[0])
print("Linha 2:",matriz.mean(axis=0)[1])
print("Linha 3:",matriz.mean(axis=0)[2])
print("Linha 4:",matriz.mean(axis=0)[3])

print("Media das colunas")
print("Coluna 1:",matriz.mean(axis=1)[0])
print("Coluna 2:",matriz.mean(axis=1)[1])
print("Coluna 3:",matriz.mean(axis=1)[2])
print("Coluna 4:",matriz.mean(axis=1)[3])

#Exercicio 4
print("------------------------Exercicio 4------------------------")
print("Numeros unicos:",np.unique(matriz, return_counts=True))
print("Numeros que aparecem duas vezes",np.unique(matriz, return_counts=True)[1]>1)




