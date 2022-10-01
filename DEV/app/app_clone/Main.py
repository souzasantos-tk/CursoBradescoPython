#Controle conta bancária.

class Main:
    pass

print('Bem Vindo! \nSenhor:')

from Cliente import Cliente
from Conta import Conta

c1= Cliente("João Gomes", "(11)9 4444-8888")
conta= Conta(c1.nome,1417, 6565, 50.88)

print(conta.titular,"\n Agencia:",conta.agencia,"\n Conta:",conta.numero,"\n Saldo:",conta.saldo)
