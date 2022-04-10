# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = input('Digite o nome: ')
while len(nome) <= 3:
    nome = input('Digite o nome: ')

idade = int(input ( 'Digite a idade: '))
while idade >= 150 or idade <= 0:
    idade = int(input('Digite a idade: '))

salario = float(input('Digite o salário: R$ '))
while salario <= 0:
    salario = float(input('Digite o salário: R$ '))

sexo = input('Digite o sexo: ')
while sexo != 'm' and sexo != 'f':
    sexo = input('Digite o sexo: ')

estado_civil = input('Estado civil: ')
while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
    estado_civil = input('Estado civil: ')


