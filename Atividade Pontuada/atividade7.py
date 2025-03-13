import os
os.system ("clear")

nome = input("Qual produto você deseja? ")
quantidade = int(input("Qual quantidade do produto? "))
preco = float(input("Qual valor do produto? "))


match quantidade:
    case 1:
        quantidade <= 5
        desconto = quantidade * 0.2
    case 2:
        quantidade > 5  <= 10
        desconto = quantidade * 0.3
    case 3:
        quantidade > 10 
        desconto = quantidade * 0.5

valor_total = desconto * preco

print()
print(f"O valor do produto é: {valor_total}")