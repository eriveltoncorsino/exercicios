"""Faça um Programa que leia três números e mostre o maior deles."""

num1 = float(input('Diga um número:'))
print('num1')

num2 = float(input('Diga mais um número:'))
print('num2')

num3 = float(input('Diga o terceiro número:'))
print('num3')

if num1 > num2 and num1 > num3:
    print('O primeiro número é o maior:', num1)

elif num2 > num1 and num2 > num3:
    print('O segundo número é o maior:', num2)

elif num3 > num2 and num3 > num1:
    print('O terceiro número é o maior:', num3)
