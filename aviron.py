# Classe représentant un bateau
class Bateau:
    def __init__(self, nom, vitesse_moyenne):
        # Initialise les attributs du bateau : nom, vitesse_moyenne, distance_parcourue
        self.nom = nom
        self.vitesse_moyenne = vitesse_moyenne
        self.distance_parcourue = 0

    def rame(self):
        # Méthode pour simuler l'avancement du bateau lors d'une rame
        self.distance_parcourue += self.vitesse_moyenne

    def obtenir_distance_parcourue(self):
        # Méthode pour obtenir la distance totale parcourue par le bateau
        return self.distance_parcourue

    def obtenir_nom(self):
        # Méthode pour obtenir le nom du bateau
        return self.nom


# Classe représentant une course d'avirons
# Classe représentant une course d'avirons
class Course:
    def __init__(self, type_bateau):
        # Initialise les attributs de la course : type_bateau, bateaux, en_course
        self.type_bateau = type_bateau
        self.bateaux = []
        self.en_course = False

    def ajout_bateau_ligne_depart(self, bateau):
        # Méthode pour ajouter un bateau à la ligne de départ
        if isinstance(bateau, Bateau) and type(bateau).__name__ == self.type_bateau:
            self.bateaux.append(bateau)
        else:
            print(f"Le bateau {bateau.obtenir_nom()} n'a pas pu être ajouté à la course {self.type_bateau}.")

    def depart(self):
        # Méthode pour démarrer la course
        self.en_course = True

    def en_cours(self):
        # Méthode pour vérifier si la course est en cours
        return self.en_course

    def prochaine_iteration(self):
        # Méthode pour simuler une itération de la course (une seconde)
        if self.en_course:
            for bateau in self.bateaux:
                bateau.rame()

    def affiche_positions(self):
        # Méthode pour obtenir une chaîne représentant les positions actuelles des bateaux
        positions = [f"{bateau.obtenir_nom()},{bateau.obtenir_distance_parcourue()}" for bateau in self.bateaux]
        return '\n'.join(positions)

    def vainqueur(self):
        # Méthode pour déterminer le vainqueur de la course
        vainqueur = max(self.bateaux, key=lambda bateau: bateau.obtenir_distance_parcourue())
        return f"Le vainqueur est {vainqueur.obtenir_nom()} avec une distance de {vainqueur.obtenir_distance_parcourue()}."

# Exemple d'utilisation avec le type de course 'skiff'
course_cadets = Course('skiff')
bateau_1_2x = Bateau('mickey', 62)
bateau_2_2x = Bateau('minnie', 70)
bateau_3_skiff = Bateau('picsou', 120)

course_cadets.ajout_bateau_ligne_depart(bateau_1_2x)
course_cadets.ajout_bateau_ligne_depart(bateau_2_2x)
course_cadets.ajout_bateau_ligne_depart(bateau_3_skiff)


course_cadets.depart()

while course_cadets.en_cours():
    course_cadets.prochaine_iteration()

print(course_cadets.affiche_positions())
print(course_cadets.vainqueur())
