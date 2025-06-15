# dicionario = {
#     "chave": "valor",
#     "aula": "python",
#     "casa": "amarela"

# }

# print(dicionario)

# set1 = {1, 2, 3}
# set2 = {4, 5, 6}

# setUnido = set2.union(set1)

# print(setUnido)

#------------------------------------------------------------
# Atividade Prática 1

#Solicitar a idade do usuário


#Classificar a pessoa em:
#Menor que 12 = criança

#entre 18 e 59 = adulto
#acima de 60 = idoso

# idade = int(input('Digite a sua idade: '))

# if idade < 12:
#     print('Criança')'
# elif idade >= 12 and idade <= 17:
#     print('Adolescente')
# elif idade >=18 and idade <=59:
#     print('Adulto')
# else:
#     print("Idoso")

#------------------------------------------------------------

#Atividade 2: Faça um programa que leia 3 números e informe o
# maior número e o menor.
    
# numero1 = int(input("Digite o primeiro número: "))

# numero2 = int(input("Digite o segundo número: "))

# numero3 = int(input("Digite o terceiro número: "))


# if numero1 > numero2 and numero1 > numero3:
#     print(f"{numero1} é o maior número")
# elif numero2 > numero1 and numero2 > numero3:
#     print(f"{numero2} é o maior número")
# else:
#     print(f"{numero3} é o maior número")

#------------------------------------------------------------

#Atividade 3: Faça um programa que peça 10 números inteiros,
# calcule
# e mostre a quantidade de números pares e a quantidade de números impares.

# pares = 0
# impares = 0
# soma_total = 0

# for i in range(10):
#    numeros = int(input("Digite um número: "))
#    soma_total += numeros

#    if numeros % 2 == 0:
#       print(f"{numeros} é um número par")
#       pares += 1
#    else:
#       print(f"{numeros} é um número ímpar")
#       impares += 1

# print(f"A quantidade de números pares foi {pares}, enquanto a quantidade de números ímpares foi {impares}")
# print(f"A soma total foi {soma_total}")

#------------------------------------------------------------

#Atividade 4: Faça um programa que peça para 20 pessoas a sua idade, 
# ao final o programa devera verificar se a médiade idade da turma 
# varia entre 0 e 25, 26 e 60 e maior que 60; 
# e então, dizer se a turma é jovem, adulta ou idosa, 
# conforme a média calculada.

idade_turma = 0

for i in range (20):
    idade = int(input("Digite a idade do aluno: "))
    idade_turma += idade

print(idade_turma)
if (idade_turma / 20) <= 25:
    print("Essa é uma turma jovem")
elif 26 <= (idade_turma / 20) <= 59:
    print("Essa é uma turma adulta")
else:
    print("Essa é uma turma idosa")
#------------------------------------------------------------