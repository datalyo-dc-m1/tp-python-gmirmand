grades = [8, 12, 15, 6, 10, 19, 18, 7, 13, 15, 8, 15, 17, 13, 12, 15, 16, 9, 10, 3, 19, 20, 15]

nbEleve = len(grades)
print('Il y a ', nbEleve, 'élèves')

noteMax = max(grades)
noteMin = min(grades)

print('Il y a un écart de ', noteMax - noteMin, 'entre la meilleur et la pire note')

grades.append(14)
nbEleve = len(grades)
print('La note de 14 a été ajoutée', grades)

grades[4] = 13
print('La 5e note a été changée en 13', grades)

moyenne = sum(grades) / nbEleve
print('La moyenne de la classe est de', moyenne)

# Utiliser sorted() ou faire un grades.sort() avant
median = sorted(grades)[int(nbEleve/2)]
print('La médiane est', median)

nbOK = 0
nbRattrapage = 0
for note in grades:
    if note >= 10:
        nbOK += 1
    elif note >= 8:
        nbRattrapage += 1

print('Il y a ', nbOK, 'élèves qui ont validé leur matière')
print('Il y a ', nbRattrapage, 'élèves qui sont en rattrapage')
