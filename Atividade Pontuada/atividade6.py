import os
os.system("clear")

primeira_nota = float(input("Digite sua primeira nota: "))
segunda_nota = float(input("Digite sua segunda nota: "))


media = (primeira_nota + segunda_nota ) /2

print()
print ("Sua média é: ", media)

if media >= 6:
    print("Aprovado")
elif media == 4 and 5:
    print("Recuperação")
else:
    print("Reprovado")