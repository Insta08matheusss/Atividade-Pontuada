import os

os.system("clear")

primeiro_numero = int(input("Digite o primeiro número: "))
operacao = input("Qual tipo de operação desejada?: ")
segundo_numero = int(input("Digite seu segundo número: "))


match operacao:
    case "+":
        resultado = soma = primeiro_numero + segundo_numero
    case "/":
        resultado = divisao = primeiro_numero / segundo_numero
    case "*":
        resultado = multiplicacao = primeiro_numero * segundo_numero
    case "-":
        resultado = subtracao = primeiro_numero - segundo_numero

print()
print (f"Primeiro número: {primeiro_numero}")
print (f"Operação: {operacao}")
print (f"Segundo número: {segundo_numero}")
print (f"Resultado: {resultado}")

