"""
Le but de cet exercice est d'approximer la valeur de π (pi) avec la méthode de Monte Carlo : 
nous utiliserons deux modules pour cela : random math
random : module qui met à disposition des méthodes liées à l'aléatoire, comment la génération de nombres aléatoires
    (1) random.random() : génére un nombre aléatoire entre 0 et 1
math : module qui met à disposition des méthodes liées aux mathématiques
    (1) math.sqrt(<nombre positif>) : renvoie la racine carré du nombre

Voir le fichier 'monte_carlo_explication.md' pour les étape de l'exercice
"""

import random, math

nb_pts_interieurs = 0
nb_iterations = 1000000
for iteration in range(nb_iterations):
    x, y = random.random(),random.random()
    if math.sqrt(x**2+y**2) <=1 : #..  # condition pour tester si le point généré est à l'intérieur du cercle ou pas 
        nb_pts_interieurs+=1       # ajout au compteur 
        
print(nb_iterations, nb_pts_interieurs)
pi = 4*(nb_pts_interieurs/nb_iterations)
print(f'la valeur approximative de pi est : {pi}, le pourcentage d\'écart est de : {abs((math.pi-pi)/math.pi)*100}')
