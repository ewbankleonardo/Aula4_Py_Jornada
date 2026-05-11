#1)Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

#numeros = list(range(1,11))
#for numero in numeros:
#    print (numero)

#Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

#lings = ["Python", "Java", "C++", "JavaScript"]

#lings.remove("C++")
#lings.append("Ruby")

#print(lings)


#Crie um dicionário para armazenar informações de um livro, 
# incluindo título, autor e ano de publicação. Imprima cada informação.

#dic = {"titulo":"Ziriguidum", "Autor":"tchurubiru","ano":1994}

#for key, value in dic.items():
#   print (f"{key}, {value}")



#Escreva um programa que conta o número de ocorrências de cada caractere em 
# uma string usando um dicionário.

#def contar_caracteres(frase):
#    contagem = {}
#    for letra in frase.lower():
#        contagem[letra] = contagem.get(letra, 0)+1
#    return contagem
#
#print (contar_caracteres("Leleo thchururu"))
#
#


#Dada a lista ["maçã", "banana", "cereja"] e o 
# \dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, 
# calcule o preço total da lista de compras.

#lista = ["maçã", "banana", "cereja"]
#dics = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
#total = 0
#for item in lista:
#    total = dics.get(item,0)+total
#print (total)
#total = sum(dics[item] for item in lista)
#for item in lista, return dics[item] e soma esses retornos

#
#
#json e tipagem de dics
#import json
#from typing import Dict, TypedDict
#
#class Produto(TypedDict):
#    nome:str
#    qtd:int
#produto : Produto = {"nome":"Leozis","qtd":1000}
##ou
#livro:Dict[str, int] = {"Titulo":"jogatina selvagem", "ano":2093}
#
#carrinho:list = []
#produto1:Dict[str,int] = {"nome":"Maça", "qty":10}
#produto2:Dict[str,int]= {"nome":"Laranja", "qty":11}
#carrinho.append(produto1)
#carrinho.append(produto2)
#print(carrinho)
#
#carrinho_json = json.dumps(carrinho, indent=1, ensure_ascii=False,sort_keys=True)
#print(carrinho_json)



#6. Eliminação de Duplicatas
#Objetivo: Dada uma lista de emails, remover todos os duplicados.

#emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
#emails_limpo = set(emails)
#print(emails_limpo)


#. Filtragem de Dados
#Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
#idades = [22, 15, 30, 17, 18]

#idades_validas = [idade for idade in idades if idade>=18 ]
#print(idades_validas)


#8. Ordenação Personalizada
#Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
#
#pessoas = [
#    {"nome": "Alice", "idade": 30},
#    {"nome": "Bob", "idade": 25},
#    {"nome": "Carol", "idade": 20}
#]
#
#pessoas.sort(key = lambda pessoa:pessoa["nome"])
#print(pessoas)

#9. Agregação de Dados
#Objetivo: Dado um conjunto de números, calcular a média.

#numeros = [10, 20, 30, 40, 50]
#
#media = sum(numeros)/len(numeros)
#
#print(media)

#10. Divisão de Dados em Grupos
#Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

#valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#par:list = []
#impar:list=[]
#for i in valores:
#    if i%2 == 0:
#        par.append(i)
#    else:
#        impar.append(i)
#
#pares = [i for i in valores if i%2==0]
#impares = [i for i in valores if i%2!=0]
#
#print (f"par:{pares},impar:{impares}")

#11. Atualização de Dados
#Objetivo: Dada uma lista de dicionários representando produtos,
#  atualizar o preço de um produto específico.

#produtos = [
#    {"id": 1, "nome": "Teclado", "preço": 100},
#    {"id": 2, "nome": "Mouse", "preço": 80},
#    {"id": 3, "nome": "Monitor", "preço": 300}
#]
#
#item = int(input("Qual Item quer atualizar? "))
#valor = float(input("Digite o novo valor "))
#for produto in produtos:
#    if produto["id"] == item:
#        print(produto["id"])
#        produto["preço"]= valor
#print(produtos)

#12. Fusão de Dicionários
#Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

#dicionario1 = {"a": 1, "b": 2}
#dicionario2 = {"c": 3, "d": 4}
#dicionario = {**dicionario1, **dicionario2} #valores do 2 sobrescrevem o do primeiro, evitando key conflict 
#
#
#dici = dicionario1|dicionario2 #2 sobrescreve o primeiro
#
#dics = dicionario1.copy() #copia o 1 no dics
#dics.update(dicionario2) #o segundo sobrescreve o primeiro
#
#print (dicionario)
#print(dici)
#print (dics)


#13. Filtragem de Dados em Dicionário
#Objetivo: Dado um dicionário de estoque de produtos, 
# filtrar aqueles com quantidade maior que 0.

#estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

#filtrados = {produto:quantidade for produto, quantidade in estoque.items() if quantidade }

#print(filtrados)


#Formula de bolo
#
#novo_dicionario = {chave: valor for item in iterável if condição}
#
#Chave (key): A expressão que define qual será a chave no novo dicionário.
#
#Valor (value): A expressão que define o valor associado àquela chave.
#
#Loop (for): O iterável (lista, tupla, outro dicionário) que você está percorrendo.
#
#Condicional (if): (Opcional) Um filtro para decidir se o item entra ou não no novo dicionário.

#14. Extração de Chaves e Valores
#Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.

#dicionario = {"a": 1, "b": 2, "c": 3}


#keys = (dicionario.keys())
#values = (dicionario.values())



#15. Contagem de Frequência de Itens
#Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.

texto = "engenharia de dados"
frequencia = {}

#for caractere in texto:
#    if caractere in frequencia:
#        frequencia[caractere] += 1
#    else:
#        frequencia[caractere] = 1
for caractere in texto:
    frequencia[caractere] = frequencia.get(caractere,0) + 1


print (frequencia)