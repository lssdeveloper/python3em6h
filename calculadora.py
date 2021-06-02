class Calculadora:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def soma(self):
        resultado = self.a + self.b
        self.impressao(resultado)

    def subtracao(self):
        resultado = self.a - self.b
        self.impressao(resultado)

    def impressao(self, a):
        print(a)
'''
calculadora1 = Calculadora(3, 2)
soma = calculadora1.soma()
subtracao = calculadora1.subtracao()
calculadora1.impressao(soma)
calculadora1.impressao(subtracao)
'''