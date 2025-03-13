import os
os.system ("clear")

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o sengundo número: "))
terceiro_numero = int(input("Digite o terciro numero: "))

soma = (primeiro_numero + segundo_numero)

maior_numero = max(soma, terceiro_numero)
menor_numero = min(soma, terceiro_numero)

print()
print(f"Soma: {soma}")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")

if primeiro_numero + segundo_numero > terceiro_numero:
    print("A soma do primeiro e do segundo número são maiores que o terceiro!")
elif primeiro_numero + segundo_numero == terceiro_numero:
    print("A soma do primeiro e do sengundo numero são iguais ao terceiro!")
else:
    print("A soma do primeiro numero mais o sengundo são menores que o terceiro!")