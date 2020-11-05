#!/usr/bin/env python3

#1 criando dicionário com as coisas favoritas

fav_dict = { 'comida' : 'lasanha', 'banda' : 'arctic monkeys', 'flor' : 'rosa', 'organismo' : 'virus', 'livro' : 'a sombra do vento', 'árvore' : 'ipê roxo' }

print(fav_dict) 

#2 imprimindo livro favorito

print(fav_dict['livro'])

#3 imprimindo livro favorito usando uma variável

fav_thing = 'livro'
print(fav_dict[fav_thing])

#4 imprimindo árvore favorita

print(fav_dict['árvore'])

#5 adicionando organismo favorito

fav_thing = 'organismo'
print(fav_dict[fav_thing]) 

#6 favorite thing do usuario

print(fav_dict.keys())
usuario = str(input("\n write your favorite thing: "))
print(fav_dict[usuario])

#7 alterando o valor de 'organismo'

fav_dict['organismo'] = 'bacteria'
print(fav_dict) 

#8 nova favorite thing do usuario 

usuario = str(input("\n write your favorite thing: "))
valor = str(input("\n write the new value for that thing: "))
fav_dict[usuario] = valor
print(fav_dict)

#9 usando loop for para imprimir as keys e valores do dicionário

for key, value in fav_dict.items() :
    print (key," : ", value)


