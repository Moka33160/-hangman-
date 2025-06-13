from wonderwords import RandomWord
import string

GAME_STATE = None
alphabet = string.ascii_lowercase
letter = list(alphabet)

def generationDuMotAleatoire(difficulte) :

    try :
        random_Word = RandomWord()
        if(difficulte == 1):
            mot = random_Word.word(word_min_length=2 ,word_max_length=5)
 
        elif(difficulte == 2 ):
            mot = random_Word.word(word_min_length=7 ,word_max_length=10)
     
        elif(difficulte == 3) :
            mot = random_Word.word(word_min_length=12 , word_max_length=15)

        else :
            mot = random_Word.word(word_min_length=15 , word_max_length=25)
        return mot
    except :
        raise Exception("erreur lors de la creation du mot")


def symbolMot(mot) :
    try :
        tab = []
        for i in mot:
            tab.append('_')
        return tab
    except :
        raise Exception("erreur lors de la symbolisationation du mot")


def bonne_Lettre(let) :
    try :
        if(let in letter) :
            return let
        return False
    except :
        raise Exception("erreur lors de la verification de la contenance de la lettre")
    

        
