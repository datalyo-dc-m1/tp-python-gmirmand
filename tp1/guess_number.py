from random import randint

number_to_guess = randint(0, 100)
print(number_to_guess)

user_propal = -1
nbtry = 0
won = False

while won == False:
    while user_propal > 10 or user_propal < 0:
        user_propal = int(input('Saisir un nombre entre 0 et 100 : '))

    if user_propal != number_to_guess:
        if nbtry <= 5:
            print('Eh non ! Ce n\'est pas', user_propal)
            user_propal = -1
            nbtry += 1
            print(nbtry)
        else:
            print('Perdu.. :( c\'étais le chiffre', number_to_guess)
    else:
        won = True

print('Bien joué ! C\'étais le', number_to_guess)
