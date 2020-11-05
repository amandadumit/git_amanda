#!/usr/bin/env python3

#criando dicionário com as coisas favoritas

fav_dict = { 'comida' : 'lasanha', 'banda' : 'arctic monkeys', 'flor' : 'rosa', 'organismo' : 'virus' }

print(fav_dict) 

print(fav_dict['comida'])

fav_thing = 'comida'
print(fav_dict[fav_thing])

print(fav_dict['flor'])

fav_thing = 'organismo'
print(fav_dict[fav_thing]) 

#alterando o valor de 'organismo'

fav_dict['organismo'] = 'bacteria'
print(fav_dict) 

