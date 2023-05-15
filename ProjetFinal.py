from datetime import datetime
from pathlib import Path
import jsonpickle
class Personne:
    def __init__(self,nom:str="Aaaaaaa",prenom:str="Aaaaaaa"):
        self.set_nom(nom)
        self.set_prenom(prenom)

    def get_nom(self):
        return self._nom

    def set_nom(self,value):
        if value[0].isupper() and 6 < len(value) < 20:
            self._nom = value
        else:
            raise ValueError("la valeur doit commencer par une majuscule et avoir entre 6 et 20 charactères")
    def get_prenom(self):
        return self._prenom

    def set_prenom(self,value):
        if value[0].isupper() and 6 < len(value) < 20:
            self._prenom = value
        else:
            raise ValueError("la valeur doit commencer par une majuscule et avoir entre 6 et 20 charactères")

    def __str__(self):
        return f"son nom:{self._nom},son prenom:{self._prenom}"

class Employe(Personne):
    def __init__(self,code:int=0,fonction:str="",nom:str="Aaaaaaa",prenom:str="Aaaaaaa"):
        self.set_code(code)
        self.set_fonction(fonction)
        super.__init__(nom,prenom)

    def get_code(self):
        return self.__code

    def set_code(self,value:int):
        self.__code=value
    def get_fonction(self):
        return self.__fonction
    def set_fonction(self,value:str):
        self.__fonction = value
    def __str__(self):
        return f"voici la fonction de{self.get_prenom()}{self.get_nom()}:code{self.__code}fonction:{self.__fonction}"

class Client(Personne):
    def __init__(self,telephone:str="111-111-1111",courriel:str="vide@pasdecourriel.com",nom:str="Aaaaaaa",prenom:str="Aaaaaaa"):
        self.set_telephone(telephone)
        self.set_courriel(courriel)
        super.__init__(nom,prenom)
    def get_telephone(self):
        return self.__telephone

    def set_telephone(self,value:str):
        self.__telephone = value

    def get_courriel(self):
        return self.__courriel

    def set_courriel(self,value:str):
        self.__courriel = value
    def __str__(self):
        return f"voici les informations de{self.get_prenom()}{self.get_nom()}:code{self.__telephone}fonction:{self.__courriel}"


class Reparation:
    def __init__(self,code:int=0,description:str="",montant:float=0.0,datereparation:datetime=datetime.now(),codeemploye:int=0):
        self.set_code(code)
        self.set_description(description)
        self.set_montant(montant)
        self.set_datereparation(datereparation)
        self.set_codeemploye(codeemploye)

    def get_code(self):
        return self.__code
    def set_code(self,value):
        self.__code=value

    def get_description(self):
        return self.__description

    def set_description(self,value:str):
        self.__description = value

    def get_montant(self):
        return self.__montant

    def set_montant(self,value:float):
        self.__montant = value

    def get_datereparation(self):
        return self.__datereparation

    def set_datereparation(self,value:datetime):
        self.__datereparation = value

    def get_codeemploye(self):
        return self.__codeemploye

    def set_codeemploye(self,value:int):
        self.__codeemploye = value
    def __str__(self):
        return f"le code est de:{self.__code}voici la description{self.__description}\n le montant total est de{self.__montant}.\ndate de reparation{self.__datereparation} par employé numero{self.__codeemploye}"


class Voiture():
    def __init__(self,numeroplaque:str="A1AA1A",marque:str="",modele:str="",couleur:str="",annee:int=0,proprietaire:Client=Client(),reparations:list[Reparation]=[]):
        self.set_numeroplaque(numeroplaque)
        self.set_marque(marque)
        self.set_modele(modele)
        self.set_couleur(couleur)
        self.set_annee(annee)
        self.set_proprietaire(proprietaire)
        self.set_reparations(reparations)

    def get_numeroplaque(self):
        return self.__numeroplaque
    def set_numeroplaque(self,value):
        self.__numeroplaque = value

    def get_marque(self):
        return self.__marque
    def set_marque(self,value):
        self.__marque = value

    def get_modele(self):
        return self.__numeroplaque
    def set_modele(self,value):
        self.__modele = value

    def get_couleur(self):
        return self.__couleur
    def set_couleur(self,value):
        self.__couleur = value

    def get_annee(self):
        return self.__annee
    def set_annee(self,value):
        self.__annee = value

    def get_proprietaire(self):
        return self.__proprietaire
    def set_proprietaire(self,value):
        self.__proprietaire = value

    def get_reparation(self):
        return self.__reparations
    def set_reparations(self,value):
        self.__reparations= value

    def __str__(self):
        return f"information sur la voiture:{self.__numeroplaque}\n{self.__modele}{self.__modele}\n{self.__couleur}\n{self.__proprietaire}{self.__annee}"


class Garage():
    def __init__(self,nom:str="",adresse:str="",telephone:str="",employes:list[Employe]=[],voitures:list[Voiture]=[]):
        self.set_nom(nom)
        self.set_adresse(adresse)
        self.set_telephone(telephone)
        self.set_employes(employes)
        self.set_voitures(voitures)

    def get_nom(self):
        return self.__nom
    def set_nom(self,value):
            self.__nom = value

    def get_adresse(self):
        return self.__adresse
    def set_adresse(self,value):
        self.__adresse = value

    def get_telephone(self):
        return self.__telephone

    def set_telephone(self,value):
            self.__telephone = value

    def get_employes(self):
        return self.__employes
    def set_employes(self,value:list[Employe]):
        self.__employes=value


    def get_voitures(self):
        return self.__voitures
    def set_voitures(self,value:list[Voiture]):
        self.__voitures = value
    @classmethod
    def serealisergarage(cls,element:object,fichier:str)->None:
        #ouvrir le fichier (creer le stream)
        path:Path=Path(fichier)
        stream=path.open('w')
        #serialiser la valeur vers le fichier
        strjson:str=jsonpickle.encode(element, indent=4,separators=(',',':'))
        #écrire le string vers le fichier
        stream.write(strjson)

        #fermer le stream
        stream.flush()
        stream.close()

    @classmethod
    def deserealisergarage(cls,fichier:str)->object:
        #ouvrir le fichier (creer le stream)
        path:Path=Path(fichier)
        stream=path.open('r')
        #deserialiser le fichier vers un objet etudiant
        strjson=stream.read()
        #réséaliser la chaine vers un objet
        reponse:object=jsonpickle.decode(strjson)

        #fermer le stream
        stream.close()
        #retourner le resultat
        return reponse
    def ajout_vouture(self,element:Voiture)->None:
        pass
