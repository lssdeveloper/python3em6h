print('########################################')
print('###### Bem-vindo ao jogo da forca!######')
print('########################################')

palavra_secreta = 'banana'
letras_acertadas = []
countLetra = 0
while len(palavra_secreta) > countLetra:
    letras_acertadas.append('_')
    countLetra += 1

acertou = False
enforcou = False
erros = 0

print(letras_acertadas)

while (not acertou and not enforcou):

    chute = input('Qual a letra?')

    if (chute in palavra_secreta):
        posicao = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                print('Encontrei a letra %s na posição %d .' % (letra, posicao))
                letras_acertadas[posicao] = letra
            posicao += 1
    else:
        erros += 1

    acertou = '_' not in letras_acertadas
    enforcou = erros == 6
    print(letras_acertadas)

if (acertou):
    print('Você ganhou!!!')
else:
    print('Você perdeu!!!')
print('Fim do Jogo')
