import os
os.system("clear")

print("""

=========== MENU ==========
Cor         \tPreço              
Verde      \t10,00     
Azul          \t20,00
Amarelo    \t 30,00
Vermelho      \t40,00
""")

cor = input("Qual cor você deseja? "). lower()
resultado = 0

match cor:
    case "verde":
        cor = "verde"
        resultado = "10,00"
    case "azul": 
        cor = "azul"
        resultado = "20,00"
    case "amarelo":
        cor = "amarelo"
        resultado = "30,00"
    case "vermelho":
        cor = "vermelho"
        resultado = "40,00"

print()
print(f"Cor: {cor}")
print(f"Valor: R$ {resultado}")