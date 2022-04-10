#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
#mostrando uma mensagem de erro e voltando a pedir as informações.

nome = input('Digite o usuário: ')
senha = input('digite a senha: ')

while senha == nome:
        print('A senha não pode ser igual ao usuário. Digite corretamente:')
        nome = input('Digite o usuário: ')
        senha = input('digite a senha: ')
print('Dados cadastrados com sucesso!')