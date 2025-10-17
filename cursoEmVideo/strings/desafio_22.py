nomeCompleto = str(input("Digite seu nome completo: "))
nomeSemEspaco = len(nomeCompleto.replace(' ', ''))
primeiroNome = nomeCompleto.split()

print(f'Seu nome completo em minúsculo é {nomeCompleto.lower()}')
print(f'Seu nome completo em maiúsculo é {nomeCompleto.upper()}')
print(f'Seu nome completo sem espaços possui {nomeSemEspaco} letras')
print(f'Seu primeiro nome é {primeiroNome[0]} e ele tem {len(primeiroNome[0])} letras')