# Programme FizzBuzz

# Boucle itérant sur les nombres de 1 à 100 inclus
for nombre in range(1, 101):
    # Vérifier les multiples de trois et cinq
    if nombre % 3 == 0 and nombre % 5 == 0:
        print("FizzBuzz")
    # Vérifier les multiples de trois
    elif nombre % 3 == 0:
        print("Fizz")
    # Vérifier les multiples de cinq
    elif nombre % 5 == 0:
        print("Buzz")
    # Afficher le nombre pour les autres cas
    else:
        print(nombre)