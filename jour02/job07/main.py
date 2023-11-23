# Chaîne de caractères
chaine_originale = "abcdefghijklmnopqrstuvwxyz" * 10

# Nombre de caractères à afficher par ligne
caracteres_par_ligne = 1

# Boucle pour afficher la suite pyramidale
for i in range(len(chaine_originale)):
    print(chaine_originale[i], end=' ')
    caracteres_par_ligne -= 1

    # Passer à la ligne et ajuster le nombre de caractères pour la ligne suivante
    if caracteres_par_ligne == 0:
        print()
        caracteres_par_ligne = 2 * (i + 1)