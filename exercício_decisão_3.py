"""Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido."""

sexo = input('Digite F para Feminino ou M para Masculino:')

if sexo == 'f':
    print ('Feminino')
elif sexo == 'm':
    print ('Masculino')
else: # qualquer outra letra
    print ('Sexo Inválido')