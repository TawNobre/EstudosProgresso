import math
#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

numero = float(input('Digite um número: '))

inteiro = math.trunc(numero)

print(f'O número {numero} tem a parte inteira = {inteiro}')
