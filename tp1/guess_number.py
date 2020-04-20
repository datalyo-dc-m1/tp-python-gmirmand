from random import randint

number_to_guess = randint(0, 10)
print(number_to_guess)

user_propal = -1
won = False

while won == False:
    while user_propal > 10 or user_propal < 0:
        user_propal = int(input('Saisir un nombre entre 0 et 10 : '))

    if user_propal != number_to_guess:
        print('Eh non !')
        user_propal = -1
    else:
        won = True


print('Bien joué ! C\'étais le', number_to_guess)




