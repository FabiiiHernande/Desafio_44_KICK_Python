# 5) Faça um programa que recebe uma string digitada pelo usuário, o programa deve exibir todas as letras que compõem a palavra digitada.  

palavra = input("Digite uma palavra: ").lower()
letras = ""

for caractere in palavra:
        letras += caractere

print("Letras na palavra digitada:")
for letra in (letras):
    print(letra)





      
    