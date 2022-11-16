1# Créer une calculatrice d'IMC demandant à l'utilisateur sa grandeur(en mètres), son poids(en kg). 
# Retournez ensuite la catégorie dans laquelle se trouve la personne.

def calcul_imc():
    grandeur = float(input('Entrez votre grandeur en mètre:'))
    poids = float(input('Entrez votre poids en kg:'))
    imc = poids / (grandeur**2)
    return imc

def catégorie():
    imc = calcul_imc()
    if imc < 18.5:
     print('Poids insuffisant:')
    elif  18.5 <= imc < 25:
        print('Poids normal:')
    elif 25 <= imc < 30:
        print('Excès de poids')
    elif 30 <= imc < 35:
        print('Obésité classe 1:')
    elif 35 <= imc < 40:
        print('Obésité classe 2:')
    elif imc > 40:
        print('Obésité classe 3:')
catégorie()                        
    