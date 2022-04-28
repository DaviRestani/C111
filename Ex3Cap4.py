import numpy as np

arr = np.loadtxt('space.csv', delimiter=';',dtype = 'str',encoding='utf-8')

#Exercicio 1
print("-----Exercicio 1-----")

status_missao = arr[1:, 7]

missoes_sucedidas = len(status_missao[np.char.find(status_missao,'Success') == 0])
porcentagem = missoes_sucedidas/len(status_missao)*100
print('Porcentagem de missões que deram certo: ', porcentagem)


#Exercicio 2
gastos = arr[1:,6].astype(float)

q_gastos = sum(gastos[gastos > 0])
n_gastos = len(gastos[gastos > 0])
media_gastos = q_gastos/n_gastos

print("Media de gastos =  ", media_gastos)

#Exercicio 3
paises = arr[1: 2]
usa = np.char.find(paises,'USA') > 0

print("Missoes realizadas pelo Estados Unidos = ", len(paises[usa]))

#Exercicio 4
empresa = arr[1:, 1]
#Já utilizando a variável de gastos do exercício 2
spacex = np.where(empresa == 'SpaceX')
custo_max = max(gastos[spacex])
print("Gasto da missao mais cara da SpaceX = ",custo_max)

#Exercicio 5
(x, y) = np.unique(empresa, return_counts=True)

for i in range(len(x)):
    print("Empresa:{}, Numero de missoes: {}".format(x[i],y[i]))


