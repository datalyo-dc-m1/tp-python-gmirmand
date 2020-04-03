"""
ex1
"""
print("=============================")
valeur = int(input("saisir un entier: "))
print("========= ex1 ==========")

carre = valeur**2
print(carre)
print(type(carre))

"""
ex2
"""
print("========= ex2 ==========")
print("Boucle Pour:")
for i in range(0, 21, 2):  # pour i allant de 0 à 20 par pas de 2
    print(f"--> i vaut: {i}")  # je repète l'action 20 fois

"""
ex3
"""
print("========= ex3 ==========")
somme = 0
for i in range(1, valeur+1, 2):  # pour i allant de 0 à 20 par pas de 2
    somme += i

print(f"somme des n premiers nombre = {somme}")


"""
ex4
"""
print("========= ex4 ==========")
if 1 < valeur < 100:
    print(f"{valeur} doit être compris entre 1 et 100")
else:
    for i in range(1, valeur+1):
        print(f"--> i vaut : {i}")