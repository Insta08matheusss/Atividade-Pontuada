import os
os.system ("clear")

nome = input("Digite seu nome?: ")
sexo = input("Qual seu sexo?: ")
estado_civil = input("Estado civil: ").lower()

if estado_civil == "casado" and "casada":
   resultado = input("Quanto tempo de casado(A)?: ")

print()
print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado civil: {estado_civil}")
print(f"Tempo de casado(A): {resultado}")