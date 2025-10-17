import random
numero = random.randint(0,10)
escolha = int(input('Escolha um número de 1 a 10: '))

if escolha == numero:
    print(f'Parabéns, você acertou! O número escolhido pelo computador era{numero}')
else:
    print(f'Que pena, não foi desssa vez! O número escolhido pelo computador foi {numero} e você digitou {escolha}')