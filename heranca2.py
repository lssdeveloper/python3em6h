class Pai:

    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso

class Filho(Pai):

    def __init__(self, nome, idade, peso, cabelo):
        #super(Filho, self).__init__(nome, idade, peso)
        super().__init__(nome, idade, peso)
        self.cabelo = cabelo

pai1 = Pai('Leandro', 45, 105)

filho1 = Filho('Amanda', 23, 60, 'Liso')
filho2 = Filho('Leana', 16, 55, 'Liso')

print(pai1.nome)
print(pai1.peso)
print(pai1.idade)

print('*******')

print(filho1.nome)
print(filho1.idade)
print(filho1.peso)
print(filho1.cabelo)