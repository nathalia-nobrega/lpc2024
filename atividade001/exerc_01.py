# Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e
# armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido.
# Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios,
# simulando os lançamentos dos dados.

import random as rand

dados = []
vezes = [0, 0, 0, 0, 0, 0]

# Lançando o dado 100 vezes e armazenando os valores dentro de um vetor
for _ in range(100):
    rand_num = rand.randint(1, 6)

    # Verificando se o número gerado já se encontra no vetor
    # Se sim, incrementa o número de vezes no vetor 'vezes',  no índice respectivo do número gerado
    if rand_num == 1:
        vezes[0] += 1
    elif rand_num == 2:
        vezes[1] += 1
    elif rand_num == 3:
        vezes[2] += 1
    elif rand_num == 4:
        vezes[3] += 1
    elif rand_num == 5:
        vezes[4] += 1
    else:
        vezes[5] += 1

    dados.append(rand_num)

for i in range(6):
    print("NÚMERO\t\t\tQUANTIDADE DE APARIÇÕES")
    print(f"{i + 1}\t\t\t\t{vezes[i]}")
