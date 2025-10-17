frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra A aparece {frase.count('A')} vezes na frase')
print(f'A letra A aparece pela primeira vez na posição {frase.find('A')+1}')
print(f'A letra A aparece pela primeira vez na posição {frase.rfind('A')+1}') 