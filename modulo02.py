#Desafios do curso "Python para Data Science" da Alura
import os
os.system("cls")

"""
1. Crie um programa que solicite à pessoa usuária digitar seu nome, e imprima “Olá, [nome]!.
"""

nome_usuario = input("Digite o seu nome:")

print("Olá, {}". format(nome_usuario))
print("")

"""
2 . Crie um programa que solicite à pessoa usuária digitar seu nome e idade, e imprima “Olá, [nome], você tem [idade] anos.”.
"""

nome_usuario2 = input("Digite o seu nome:")
idade_usuario = input("Digite a sua idade:")
print("")

print("Olá, {}, você tem {} anos.".format(nome_usuario2, idade_usuario))
print("")

"""
3. Crie um programa que solicite à pessoa usuária digitar seu nome, idade e altura em metros, e imprima 
“Olá, [nome], você tem [idade] anos e mede [altura] metros!”.
"""

nome_usuario3 = input("Digite o seu nome:")
idade_usuario2 = input("Digite a sua idade:")
altura_usuario = input("Digite a sua altura:")
print("")

print("Olá, {}, você tem {} anos e mede {} metros!".format(nome_usuario3, idade_usuario2, altura_usuario))


