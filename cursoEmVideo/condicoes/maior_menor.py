numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

lista = [numero1, numero2, numero3]
lista_ordenada = sorted(lista)

print(f"O menor número é {lista_ordenada[0]}")
print(f"O maior número é {lista_ordenada[2]}")