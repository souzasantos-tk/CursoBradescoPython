#Estrutura de Decisão Composta ou Estrutura Condicional
idade = int (input("Digite a Idade: "))

if idade >= 18:
    print("Maior de Idade")
elif idade >= 16:
    print("Juvenil")
elif idade >= 12:
    print("Adolescente")
else:
    print("Menor de Idade")
