#!usr/bin/python3.6m
#-*-coding:utf-8-*

from math import ceil
from random import randrange
from zcasino_modules import pair

argent = 100
rejouer = 'O'

print("Bonjour! \nBienvenue à la table du jeu de roulette.\nVous avez acheté pour 100$ de jetons à l'entrée du casino.")

while rejouer == 'o' or rejouer == 'O' or argent >0 : 

	num = randrange(50)
	pair_num = pair(num)	# ma fonction pair dans zcasino_modules.py -> renvoie True si num nombre pair

	# TRAITEMENT DE LA MISE
	mise = input ("\nCombien misez-vous (veuillez saisir un nombre entier) ? -> ")

	# Forcer la saisie d'une valeur (empêcher variable vide)
	while not mise : 
		print("\nVous n'avez rien saisi. Vérifiez que votre clavier numérique est activé.")
		mise = input ("Saisissez à nouveau votre mise -> ")

	# Vérifier que la mise saisie est valide -> un nombre entier inférieur ou égal à la somme dont dispose le joueur. 
	while type(mise) != 'int' or mise > argent or mise <= 0 : 
		try: 
			mise = int(mise)
			assert mise <= argent
			if mise <=0 : raise ValueError
		except ValueError: 
			print("\nErreur : vous avez saisi un nombre invalide \
(vérifiez qu'il s'agit bien d'un nombre entier et >0)")
			mise = input("Saisir à nouveau -> ")
		except AssertionError : 
			print("\nErreur : vous avez saisi plus que vous ne possédez. \nIl vous reste actuellement ", argent , "$.")
			mise = input("Saisir à nouveau -> ")
		else : 
			break

	# TRAITEMENT DU NUMÉRO MISÉ
	num_mise = input ("\nSaisissez maintenant le numéro sur lequel vous misez \n(un numéro de 0 à 49 inclus) -> ")

	while not num_mise : 
		print("\nVous n'avez rien saisi. Vérifiez que votre clavier numérique est activé.")
		num_mise = input("Saisir à nouveau -> ")

	while True : 
		try : 
			num_mise = int(num_mise)
			assert num_mise <=49 and num_mise >=0
		except ValueError: 
			print("Erreur : vous avez saisi un nombre invalide (vérifiez qu'il s'agit bien d'un nombre entier)")
			num_mise = input ("Saisir à nouveau -> ")
		except AssertionError : 
			print("Erreur : vous n'avez pas saisi un nombre compris de 0 à 49 inclus.")
			num_mise = input ("Saisir à nouveau -> ")
		else : 
			break

	pair_num_mise = pair(num_mise)		# ma fonction pair dans zcasino_modules.py -> renvoie True si nombre pair

	print("Vous avez misé " , mise , "$ sur le " , num_mise , ". C'est parti ! ... ")

	print("\n...")
	print("\n...")
	print("\n...")

	print ("Le numéro gagnant est le " , num)

	if num_mise == num : 
		print("Bravo ! Vous avez joué le numéro gagnant et remportez 3 fois votre mise !\nVous gagnez donc " , 3*mise , "$.\n")
		argent = argent + 3*mise
		print("Votre cagnotte se monte maintenant à " , argent , "$ !!!")
	elif pair_num == pair_num_mise : 
		argent = argent + mise/2
		argent = ceil(argent)			# arrondi supérieur pour cas de nombre réel (conversion entier 'int')
		print("Bravo ! Vous avez joué la bonne couleur et remportez la moitié de votre mise !\nVous gagnez donc " , ceil(mise/2) , "$.")
		print("Votre cagnotte se monte maintenant à " , argent , "$.")
	else : 
		print("Dommage, vous avez perdu votre mise. Votre cagnotte se monte maintenant à ", argent - mise , "$.")
		argent = argent - mise

	if argent <= 0 : 
		print("Vous êtes fauché ! Votre cagnotte est vide ! \nLe ZCasino vous remercie de votre visite.:-)")
		break
	else : 
		rejouer = input("Voulez-vous rejouer ?(O/N)")
		if rejouer == 'N' or rejouer == 'n': 
			print("Le ZCasino vous remercie de votre visite. A bientôt !")
			break

# python3.6m zcasino.py

