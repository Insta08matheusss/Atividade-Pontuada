import os
os.system("clear")

import os
os.system("clear")

print("""

=========== MENU ==========
Código   \tAté 5kg               \tAcima de 5kg
Morango      \tR$2,50 por Kg      \tR$2,20 por Kg
Maçã          \tR$1,80 por Kg    \tR$1,50 por Kg


""")

maca = float(input("Digite a quantidade de maçã: "))
morango = float(input("Digite a quantidade de morango: "))

if morango <= 5:
    preco_mo = 2.50
else:
    preco_mo = 2.20

if maca <= 5:
    preco_ma = 1.80
else:
    preco_ma = 1.50

valormo = morango * preco_mo
valorma = maca * preco_ma
valordinheirot = valormo + valorma
kgtotal = morango + maca



if valordinheirot >= 50 or kgtotal >= 8:
    desconto = valordinheirot * 0.10
    valordinheirot = valordinheirot - desconto
print(f"O valor total a ser pago é de R${valordinheirot:.2f}")
print(f"Você comprou {kgtotal} KG de frutas")