class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

class Auteur:
    def __init__(self, nom):
        self.nom = nom


auteur1 = Auteur("J.K. Rowling")
livre1 = Livre("Harry Potter and the Sorcerer's Stone", auteur1)
livre2 = Livre("Harry Potter", auteur1)

class Bibliotheque:
    def __init__(self):
        self.collection = []
        
    def emprunter_livre(self, livre):
        if livre in self.collection:
            self.collection.remove(livre)
            print( "Le livre a ete emprunte")
        else:
            return print("Le livre n'est pas disponible")
        
    def ajouterLivre(self, livre):
        self.collection.append(livre)
        
        
        
bibliotheque = Bibliotheque()
bibliotheque.ajouterLivre(livre2)
resultat = bibliotheque.emprunter_livre(livre2)
        
    