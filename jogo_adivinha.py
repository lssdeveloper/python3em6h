import random

print('########################################')
print('Bem-vindo ao jogo do adivinha o número!')
print('########################################')

chances = 7
nro_tentaivas = 1
numero_sorteado = random.randint(1, 100)
print(numero_sorteado)

jogador = input('Informe o seu nome:')


while nro_tentaivas <= 7:
    palpite = int(input('Informe um número de 1 até 100'))
    if palpite < numero_sorteado:
        print('Você errou. Seu número é menor que o sorteado, tente novamente.')
        print('Tentativa %d de %d' % (nro_tentaivas, chances))
    elif palpite > numero_sorteado:
        print('Você errou. Seu número é maior que o sorteado, tente novamente.')
        print('Tentativa %d de %d' % (nro_tentaivas, chances))
    elif palpite == numero_sorteado:
        print('PARABÉNS!!!', jogador)
        nro_tentaivas = 7

    if nro_tentaivas == 6:
        print('Última tentaiva!')
    elif nro_tentaivas == 7:
        print('### FIM DE JOGO ###')

    nro_tentaivas += 1