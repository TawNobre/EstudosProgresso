cidade = str(input('Em que cidade você nasceu? '))
cidadeOrganizada = cidade.split()
santo = 'SANTO' in cidadeOrganizada[0].upper()

print(santo)