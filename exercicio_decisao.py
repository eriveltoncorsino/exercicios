"""Faça um Programa que peça dois números e imprima o maior deles."""

n1 = int(input('Diga o primeiro número:'))
n2 = int(input('Diga o segundo número:'))

if n1 > n2:
    print (n1, 'é maior que', n2)
elif n1 < n2:
    print (n2, 'é maior que', n1)
else: print ('Os números são iguais')

