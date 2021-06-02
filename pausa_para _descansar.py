'''
Criar uma função que me lembre a parar de estudar e fazer uma pausa a cada 2h
Trabalho inicia de 8h às 12
'''

import webbrowser
import time

intervalo = 2
contador = 0
print('O programa de controle de descanso foi ativado.')


while contador < intervalo:
    time.sleep(10)
