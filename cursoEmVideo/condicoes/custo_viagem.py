preco = 0
distancia = float(input("Qual a distância, em Km, da viagem que você irá fazer? "))

if distancia <= 200:
    preco = 0.50*distancia
    print(f"A viagem será de {distancia}Km, logo o valor da passagem ficará R${preco}.")
else:
    preco = 0.45*distancia
    print(f"A viagem será de {distancia}Km, logo o valor da passagem ficará R${preco}.")

print("Tenha uma boa viagem!")