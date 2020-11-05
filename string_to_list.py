#!/usr/bin/env python3

taxa = 'sapiens, erectus, neanderthalensis'


print(taxa)

#como é uma string e não lista ainda, ele vai printar o a, que é o índice 1 da string

print(taxa[1])

#para confirmar que é uma string ainda, e não uma lista

print(type(taxa))

#transformando string em lista com a função split

print(taxa.split(','))

#armazenando essa nova lista em um objeto chamado species
species = taxa.split(',')
print(species)

#agora printando o índice 1 da lista ele retornará certo

print(species[1])

#para confirmar se o tipo mudou, agora é lista e não string mais

print(type(species))

#organizar a  lista em ordem alfabética e printar

print(sorted(species, key = None))

#organizar a lista por comprimento de cada item e printar

print(sorted(species, key = len))

#print(sorted(species, key = str.len(species))) 
