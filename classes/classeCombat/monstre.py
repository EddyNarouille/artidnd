from classes.classeCombat.classeHerit import classeHerit


class Monstre(classeHerit):
    def __init__(self, user=None,nivDanger=1):
        super().__init__(user)
        self.nivDanger = nivDanger
    def increaseHP(self,nbPv) :
        nbMaxPv = int((self.user.maxpv+self.nivDanger)*(1+(self.nivDanger/5)))
        if self.user!=None and nbPv < nbMaxPv :
            self.user.maxpv = nbMaxPv
            self.user.pv = nbMaxPv
    def __str__(self):
        return f"Monstre|{self.nivDanger}"