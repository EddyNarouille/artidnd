import json
class Armure : 
    def __init__(self,nom,armure):
        self.armure = armure
        self.nom= nom
    def __str__(self):
        return f"# {self.nom} \n **valeur de protection** : {self.armure}"
    def toJSON(self) :
        return self.nom