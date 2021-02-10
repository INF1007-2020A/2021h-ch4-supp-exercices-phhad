#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def is_even_len(string: str) -> bool:
	if len(string)%2==0:
		return True
	else:
		return False


def get_num_char(string, char):
	compteur = 0
	for c in string:
		if c == char:
			compteur += 1
	return compteur


def get_first_part_of_name(name):
	Partie_1_nom = name.split("-")[0]
	return Partie_1_nom


def get_random_sentence(animals, adjectives, fruits):
	word = []
	for word_set in(animals, adjectives, fruits):
		word += [word_set[random.randrange(0, len(word_set))]]
	return  word



if __name__ == "__main__":
	spam = "Bonjour!"
	parity = "pair" if is_even_len(spam) else "impair"
	print(f"Le nombre de caractère dans la chaine '{spam}' est {parity}.")

	eggs = "Hello, world!"
	print(f"Le nombre d'occurrence de l dans '{eggs}' est : {get_num_char(eggs, 'l')}.")

	parrot = "jean-marc"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "bananes")
	print(get_random_sentence(animals, adjectives, fruits))
