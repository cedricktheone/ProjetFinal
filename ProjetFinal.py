from datetime import datetime

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
    def __init__(self,code:int=0,fonction:str="",,nom:str="Aaaaaaa",prenom:str="Aaaaaaa"):
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
        return self.__description

    def set_codeemploye(self,value:int):
        self.__description = value
