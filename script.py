from wonderwords import RandomWord
import string


class jeux:
    GAME_STATE = None
    alphabet = string.ascii_lowercase
    letter = list(alphabet)
    cpt = 0
    mot = ""
    tab_mot = []

    def __init__(self, difficulte):
        self.difficulte = difficulte

    """_summary_
    permet de générer un mot plus ou moins long suivant la difficulté sélectionner
    """

    def generationDuMotAleatoire(self):
        random_Word = RandomWord()
        if self.difficulte == 1:
            self.mot = random_Word.word(word_min_length=2, word_max_length=5)

        elif self.difficulte == 2:
            self.mot = random_Word.word(word_min_length=7, word_max_length=10)

        elif self.difficulte == 3:
            self.mot = random_Word.word(word_min_length=12, word_max_length=15)

        elif self.difficulte == 4:
            self.mot = random_Word.word(word_min_length=15, word_max_length=25)
        tab_mot = list(self.mot)

    """_summary_
    permet de symboliser le mot par des traits
    """

    def symbolMot(self, mot):
        tab = []
        for i in mot:
            tab.append("_")
        return tab

    """_summary_
    regarde si le joueur a saisi une lettre.
    """

    def bonne_Lettre(self, let):
        if let in self.letter:
            return let
        return False

    """_summary_
    peremt de faire la perte de point 
    """

    def pertedePoint(self, let):
        if let not in self.letter:
            self.cpt += 1
        if self.difficulte == 4 & self.cpt == 3:
            self.GAME_STATE = False
        elif self.difficulte == 3 & self.cpt == 4:
            self.GAME_STATE = False
        elif self.difficulte == 2 & self.cpt == 5:
            self.GAME_STATE = False
        elif self.difficulte == 1 & self.cpt == 6:
            self.GAME_STATE = False

    """_summary_
     permet de retirer les lettres et de voir si le jouuer va gagner.
    """

    def jeux(self, choixJoueur):
        if len(self.tab_mot) == 0:
            self.GAME_STATE = True

        elif choixJoueur in self.tab_mot:
            self.tab_mot.remove(choixJoueur)
            self.letter.remove(choixJoueur)
            return choixJoueur
        self.letter.remove(choixJoueur)
        return choixJoueur
