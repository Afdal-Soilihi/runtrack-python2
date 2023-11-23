# Fonction pour déterminer le type de triangle
def type_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        # Vérifier si le triangle est rectangle
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return "rectangle"
        # Vérifier si le triangle est équilatéral
        elif a == b == c:
            return "équilatéral"
        # Vérifier si le triangle est isocèle
        elif a == b or a == c or b == c:
            return "isocèle"
        # Le triangle est quelconque
        else:
            return "quelconque"
    else:
        return "impossible"

# Saisie des longueurs a, b, et c
try:
    a = float(input("Entrez la longueur a : "))
    b = float(input("Entrez la longueur b : "))
    c = float(input("Entrez la longueur c : "))
except ValueError:
    print("Veuillez entrer des nombres valides.")
    exit()

# Appel de la fonction pour déterminer le type de triangle
type_resultat = type_triangle(a, b, c)

# Affichage du résultat
if type_resultat == "impossible":
    print("Il n'est pas possible de construire un triangle avec ces longueurs.")
else:
    print(f"Avec les longueurs {a}, {b}, et {c}, le triangle est {type_resultat}.")