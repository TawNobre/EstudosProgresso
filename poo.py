# class Cachorro:
#     def __init__(self, nome, raca, idade):
#         self.nome = nome
#         self.raca = raca
#         self.idade = idade

#     def latir(self):
#         return 'au au'
    
#     def envelhecer(self,novaIdadeDeEnvelhecimento):
#         self.idade += novaIdadeDeEnvelhecimento 

#     def informacao(self):
#         return f'{self.nome} {self.raca} {self.idade}'
    
# objetoPrimeiroCachorro = Cachorro(nome ='Bidu', raca='pinscher', idade=2)
# objetoSegundoCachorro = Cachorro(nome ='Lili', raca='pitbull', idade=5)



# objetoPrimeiroCachorro.envelhecer(novaIdadeDeEnvelhecimento=2)

# print(objetoPrimeiroCachorro.informacao())
# print(objetoSegundoCachorro.informacao())

class Carro:
    def __init__(self, marca, modelo, ano, km):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.km = km

    def informacao(self):
        return f'{self.marca, self.modelo, self.ano, self.km}'
    
    def aumentoKilometragem(self, novaKilometragem):
        self.km += novaKilometragem
    def reduzKilometragem(self,novaKilometragem):
        self.km -= novaKilometragem

    def ipva(self):
        anoAtual = 2025
        if self.ano >= anoAtual - 15:
            return 'Deve pagar o IPVA'
        else:
            return 'Não deve pagar ipva'

    



objetoPrimeiroCarro = Carro(marca='BYD', modelo='Dolphin', ano=2025, km=0)
objetoSegundoCarro = Carro(marca='Nissan', modelo='Kicks', ano=1998, km=200)

print(objetoPrimeiroCarro.informacao())
print(objetoSegundoCarro.informacao())
print(objetoSegundoCarro.ipva())