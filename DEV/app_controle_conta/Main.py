class Main:
    pass

print('Bem Vindo! \nSenhor:')

from Cliente import Cliente
from Conta import Conta

c1= Cliente("João Gomes", "(11)9 4444-8888")
conta= Conta(c1.nome, 6565, 1.58)

print(conta.titular,"\nConta:",conta.numero)

if (conta.saldo < 0):
    print("Saldo Negativo")
else:
    print("Saldo:",conta.saldo)