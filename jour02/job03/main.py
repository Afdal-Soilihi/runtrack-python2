# Programme affichant tous les nombres de 0 à 100 sauf 26, 37, 88

# Boucle parcourant les nombres de 0 à 100 inclus
for nombre in range(101):
    # Exclure les nombres spécifiques
    if nombre not in [26, 37, 88]:
        print(nombre)