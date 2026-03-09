print("Calculadora simples")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = input("Digite o número da operação: ")

if operacao == "1":
    resultado = numero1 + numero2
elif operacao == "2":
    resultado = numero1 - numero2
elif operacao == "3":
    resultado = numero1 * numero2
elif operacao == "4":
    resultado = numero1 / numero2
else:
    print("Operação inválida")
    resultado = None

if resultado != None:
    print("Resultado:", resultado)
