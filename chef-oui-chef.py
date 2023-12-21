# Fonction pour vérifier les salutations entre officiers
def check_salute(corridor):
    # Vérifie si la chaîne de caractères est valide (contient uniquement les caractères autorisés)
    if not all(char in '-<->' for char in corridor):
        return 0  # Renvoie 0 si la chaîne de caractères est invalide

    salute_count = 0  # Initialisation du compteur de salutations
    left_to_right = 0  # Initialisation du nombre d'officiers se dirigeant de gauche à droite

    # Parcourt chaque caractère dans le couloir
    for char in corridor:
        if char == '-':
            left_to_right += 1  # Incrémente le nombre d'officiers se dirigeant de gauche à droite
        elif char == '>':
            salute_count += left_to_right  # Chaque officier à gauche salue un officier à droite

    return salute_count  # Renvoie le nombre total de salutations

# Exemples d'utilisation
print(check_salute('->-------------<-------'))  # Attendu: 1
print(check_salute('-<------------->-------'))  # Attendu: 0
print(check_salute('-->>----<<--'))  # Attendu: 4
print(check_salute('--->--->----->--'))  # Attendu: 0
print(check_salute('---<---->-->----<<-->'))  # Attendu: 4
