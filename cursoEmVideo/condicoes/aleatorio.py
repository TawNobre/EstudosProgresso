import random

opcao = ['pedra', 'papel', 'tesoura']
maquina = random.choice(opcao)

print("Vamos começar a jogar pedra, papel ou tesoura.")
selecao = str(input("Escolha uma das opções para o desafio: ")).lower()

print(f"\nA máquina escolheu: {maquina.capitalize()}") 
print(f"Você escolheu: {selecao.capitalize()}\n")


if maquina == 'pedra':
    if selecao == 'pedra':
        print("Empate! Ambos escolheram Pedra.")
    elif selecao == 'papel':
        print("Parabéns! Papel ganha de Pedra.")
    elif selecao == 'tesoura':
        print("Que pena! Pedra ganha de Tesoura.")
    else:
        print("Opção inválida!")

elif maquina == 'papel': 
    if selecao == 'papel':
        print("Empate! Ambos escolheram Papel.")
    elif selecao == 'tesoura':
        print("Parabéns! Tesoura ganha de Papel.")
    elif selecao == 'pedra':
        print("Que pena! Papel ganha de Pedra.")
    else:
        print("Opção inválida!")

elif maquina == 'tesoura': 
    if selecao == 'tesoura':
        print("Empate! Ambos escolheram Tesoura.")
    elif selecao == 'pedra':
        print("Parabéns! Pedra ganha de Tesoura.")
    elif selecao == 'papel':
        print("Que pena! Tesoura ganha de Papel.")
    else:
        print("Opção inválida!")