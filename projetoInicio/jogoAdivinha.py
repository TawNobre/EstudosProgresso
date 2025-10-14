import random

numero_secreto = random.randint(1,100)
tentativa = 0

print("Seja bem-vindo ao jogo de Adivinhar o Número aleatório")
print("Eu pensei em um número de 1 a 100. Tente adivinhar!")

while True:
    tentativa += 1
    try:
        palpite_str = input("Digite o seu palpite: ")
        palpite = int(palpite_str)
    except ValueError:
        print("Opa! Isso não é um número válido, tente novamente.")
        continue

    if palpite < numero_secreto:
        print("Muito baixo! Tente um número maior.")
    elif palpite > numero_secreto:
        print("Muito alto! Tente um número menor.")
    else:
        print(f"Parabéns! Você acertou!!!! O  número era {numero_secreto}. Você finalizou em {tentativa} tentativas")
        break
