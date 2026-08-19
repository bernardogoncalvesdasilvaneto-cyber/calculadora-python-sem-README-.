print("Bem-vindo à Calculadora em Python!")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
 
soma = numero1 + numero2
print("A soma é:", soma)

subtracao = numero1 - numero2
print("A subtração é:", subtracao)

multiplicacao = numero1 * numero2
print("A multiplicação é:", multiplicacao)

if numero2 != 0:
    divisao = numero1 / numero2
    print("A divisão é:", divisao)
else:
    print("Não é possível dividir por zero!")

