# Programme affichant les tables de multiplication de 1 à N

# Fonction pour afficher la table de multiplication pour un nombre spécifique
def afficher_table_multiplication(nombre, limite):
    print(f"\nTable de multiplication pour {nombre} :")
    for i in range(1, limite + 1):
        produit = nombre * i
        print(f"{nombre} x {i} = {produit}")

# Saisie de N (entier supérieur à zéro)
while True:
    try:
        N = int(input("Entrez un entier supérieur à zéro (N) : "))
        if N > 0:
            break
        else:
            print("Veuillez entrer un entier supérieur à zéro.")
    except ValueError:
        print("Veuillez entrer un nombre entier.")

# Affichage des tables de multiplication de 1 à N
for j in range(1, N + 1):
    afficher_table_multiplication(j, 10)  # Limite de la table à 10 pour chaque nombre 