print('#################################################')
print('Bem vindo ao programa de cálculo de média escolar')
print('#################################################')
seu_nome = input('Informe o seu nome:')
sua_materia = input('Informe a matéria:')

print('Agora informe as 4 notas bimestrais:')
nota1 = float(input('Informe a 1ª nota:'))
nota2 = float(input('Informe a 2ª nota:'))
nota3 = float(input('Informe a 3ª nota:'))
nota4 = float(input('Informe a 4ª nota:'))

media = (nota1 + nota2 + nota3 + nota4)/4

if media < 7:
    print('Aluno %s, você foi REPROVADO. Sua média em %s foi de %.2f.'
        % (seu_nome, sua_materia, media))
else:
    print('PARABÉNS !!!!')
    print('Aluno %s, você foi APROVADO. Sua média em %s foi de %.2f.'
        % (seu_nome, sua_materia, media))