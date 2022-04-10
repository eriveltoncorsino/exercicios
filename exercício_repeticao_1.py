#Faça um programa que peça uma nota, entre zero e dez.
#Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = float(input('Digite sua nota: '))
while nota < 0 or nota > 10:
    print('Digite sua nota corretamente: ')
    nota = float(input('Digite sua nota: '))
print('Sua nota foi: {}.'.format(nota))