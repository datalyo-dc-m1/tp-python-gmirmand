"""
ex1
"""
carre = 0

valeur = int(input("saisir un entier: "))
carre = valeur**2
print(carre)
print(type(carre))

"""
ex2
"""
print("Boucle Pour:")
for i in range(0, 21, 2):  # pour i allant de 0 à 20 par pas de 2
    print(f"--> i vaut: {i}")  # je repète l'action 20 fois