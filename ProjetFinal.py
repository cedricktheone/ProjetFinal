class Personne:
    def __init__(self,nom:str="Aaaaaaa",prenom:str="Aaaaaaa"):
        self.set_nom(nom)
        self.set_prenom(prenom)

    def get_nom(self):
        return self.__nom

    def set_nom(self,value):
        if value[0].isupper() and 6 < len(value) < 20:
            self.__nom = value
        else:
            raise ValueError("la valeur doit commencer par une majuscule et avoir entre 6 et 20 charactères")
    def get_prenom(self):
        return self.__prenom

    def set_prenom(self,value):
        if value[0].isupper() and 6 < len(value) < 20:
            self.__prenom = value
        else:
            raise ValueError("la valeur doit commencer par une majuscule et avoir entre 6 et 20 charactères")

    def __str__(self):
        return f"son nom:{self.__nom},son prenom:{self.__prenom}"

class Employe(Personne):
        def __init__(self,code:int=0,fonction:str=""):
            super.__init__()
