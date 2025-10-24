velocidade_maxima = 80
multa = 7
excedente = 0
velocidade_motorista = float(input("Qual é a velocidade que você está dirigindo? "))

if velocidade_motorista > velocidade_maxima:
    excedente = (velocidade_motorista - velocidade_maxima) * multa
    print(f"Você passou da velocidade permitida na via, que é de 80Km/h. Terá que pagar uma multa de R${excedente:.2f}")
else:
    print("Parabéns! Você está em uma velocidade segura")
    