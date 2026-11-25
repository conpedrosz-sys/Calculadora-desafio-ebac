#!/usr/bin/env python3

print("Iniciando Calculadora")



num1 = input('digite o primeiro número: ')
num2 = input('digite o segundo número: ')

convert_valor1 = int(num1)
convert_valor2 = int(num2)



op = input('digite a operação (+, -, *, /): ')

if op == '+':
 print('O valor da soma é de:', convert_valor1 + convert_valor2)
elif op == '-':
  print('O valor da subtração é de:', convert_valor1 - convert_valor2)
elif op == '*':
  print('O valor da multiplicação é de:', convert_valor1 * convert_valor2)
elif op == '/':
  print('O valor da divisão é de:', convert_valor1 / convert_valor2)
else:
    print('Operação inválida')

