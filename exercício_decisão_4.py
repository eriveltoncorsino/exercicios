"""Faça um Programa que verifique se uma letra digitada é vogal ou consoante"""

letra = input('Digite uma letra:')

if letra.isalpha():
    if letra == 'a':
        print ('vogal')
    elif letra == 'e':
        print ('vogal')
    elif letra == 'i':
        print ('vogal')
    elif letra == 'o':
        print ('vogal')
    elif letra == 'u':
        print ('vogal')
    else: #qualquer outra letra
        print('consoante')
else: #qualquer outra letra
    print('Não é uma letra')