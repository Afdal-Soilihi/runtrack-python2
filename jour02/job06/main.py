# Programme affichant les nombres premiers jusqu'à 1000

# Fonction pour vérifier si un nombre est premier
def est_premier(nombre):
    if nombre < 2:
        return False
    for i in range(2, int(nombre**0.5) + 1):
        if nombre % i == 0:
            return False
    return True

# Boucle itérant sur les nombres de 1 à 1000 inclus
for nombre in range(2, 1001):
    if est_premier(nombre):
        print(nombre)