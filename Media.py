notaA = float(input("Digite a primeira nota: "))
notaB = float(input("Digite a segunda nota: "))

#Calcular Média
mediafinal = (notaA + notaB) / 2

#Verificação
if mediafinal >= 7.0:
    print("A Média: %.1f - Aprovado" %mediafinal)
else:
    print("A Média: %.1f - Reprovado" %mediafinal)
