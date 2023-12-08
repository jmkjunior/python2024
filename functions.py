def dictionnaire_aleatoire():
    mon_dict = {
        "root": "password"  
    }
    
    return mon_dict

#fonction salutation

def salutation(nom, age):
    """ Affiche une phrase de salutation personnalisée """
    
    # Initialise la variable age_texte avec la valeur par défaut "ans"
    age_texte = "ans"
    
    # Vérifie si l'âge est égal à 1, auquel cas met à jour age_texte à "an"
    if age == 1:
        age_texte = "an"
        
    # Affiche la salutation personnalisée en utilisant un f-string
    print(f"Bonjour '{nom}', vous avez actuellement {age} {age_texte}.")

# Appel de la fonction avec des exemples
salutation("gael", 24) 
# Affichera: Bonjour 'gael', vous avez actuellement 24 ans.

salutation("bébé", 0)
# Affichera: Bonjour 'bébé', vous avez actuellement 0 an.


#fonction power_2
def power_2(limit):
    """ Retourne une liste des puissances de 2 jusqu'à la limite spécifiée. """
    
    # Initialise une liste vide pour stocker les puissances de 2
    powers_of_2 = []

    # Boucle pour calculer les puissances de 2 et les ajouter à la liste
    for i in range(limit + 1):
        powers_of_2.append(2 ** i)

    return powers_of_2

# Exemple d'appel de la fonction
resultat = power_2(10)
print(resultat)
# Output attendu : [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

#fonction check_ip_format
def check_ip_format(ip):
    """ Vérifie si l'IP est au format IPv4. """
    
    # Vérifie la longueur et si chaque partie est un entier entre 0 et 255
    return len(ip.split('.')) == 4 and all(octet.isdigit() and 0 <= int(octet) <= 255 for octet in ip.split('.'))

# Exemples d'appel de la fonction
resultat1 = check_ip_format('10.0.0.0')
print(resultat1)
# Output attendu : True

resultat2 = check_ip_format('192.12.')
print(resultat2)
# Output attendu : False

