"""
Le but de cet exercice est d'approximer la valeur de π (pi) avec la méthode de Monte Carlo : 
nous utiliserons deux modules pour cela : random math
random : module qui met à disposition des méthodes liées à l'aléatoire, comment la génération de nombres aléatoires
    (1) random.random() : génére un nombre aléatoire entre 0 et 1
math : module qui met à disposition des méthodes liées aux mathématiques
    (1) math.sqrt(<nombre positif>) : renvoie la racine carré du nombre

Voir le fichier 'monte_carlo_explication.md' pour les étape de l'exercice
"""
from random import random
from math import pi

N = int(1e6)
P = [(random(),random()) for i in range(N)]
C = [p for p in P if pow(p[0],2)+pow(p[1],2)<=1]
PI = (4*len(C))/N

print(abs((PI-pi)/pi)*100)