import os
os.system("clear")

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o sengundo número: "))


if primeiro_numero == segundo_numero:
    soma = primeiro_numero + segundo_numero
    print(f"Soma do primeiro número e so segundo numero: {soma}")
elif primeiro_numero != segundo_numero:
    multiplicacao = primeiro_numero * segundo_numero
    print(f"Multiplicação do primeiro número e so segundo numero: {multiplicacao}")

print()
print(f"Primeiro número: {primeiro_numero}")
print(f"Segundo número: {segundo_numero}")