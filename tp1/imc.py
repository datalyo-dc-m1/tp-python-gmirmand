taille = float(input('Saisir votre tailler (en mètre) = '))
poid = float(input('Saisir votre poid (en kg)  = '))

imc = (poid / (taille * taille))
print("%.2f" % imc)

imcDescription = 'Vous êtes en état de maigreur'

if imc > 18.5:
    imcDescription = 'Vous êtes normal'
if imc > 24.9:
    imcDescription = 'Vous êtes en état de surpoid'
if imc > 29.9:
    imcDescription = 'Vous êtes en état d\'obésité'
if imc > 40:
    imcDescription = 'Vous êtes en état d\'obésité massive'

print(imcDescription)