# 5) Faça um programa que gere as tabuadas do 1 até o 10.

numero = 1

while numero != 11:
    for x in range(0, 11):
        resultado = numero * x
        print(f"{numero} x {x} = {resultado}")
        
    numero += 1
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")