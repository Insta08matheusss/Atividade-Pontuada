import os
os.system("clear")
print("""
==========TABELA===========
O valor total deve ser 10x o valor da renda mensal do solicitante
E a prestação não pode ser maior que 30% da renda mensal do solicitante
      """)



valor = float(input("Digite o valor da renda do solicitante: "))
emprestimo = float(input("Digite o valor do emprestimo: "))
parcelas = int(input("Digite a quantidade de parcelas: "))
os.system("clear")

if emprestimo <= valor * 10 and emprestimo / parcelas <= valor * 0.30:
    print("Emprestimo aceito")

else:
    print("Emprestimo negado")
    print(f"O valor do emprestimo deve ser 10x o valor da renda mensal do solicitante {valor * 10}")
    print(f"O valor da parcela não pode ser maior que 30% da renda mensal do solicitante {valor * 0.30}")
    print(f"Valor da parcela: {emprestimo / parcelas}")
    print("Quantidade de parcelas {parcelas}")
    exit()
print(f"O valor total a ser pago é de {emprestimo:.2f} R$")
print(f"O valor de cada parcela é de {emprestimo / parcelas:.2f} R$")
print(f"O total de parcelas é de {parcelas}")