from classes.classeCombat.classeHerit import classeHerit


class Monstre(classeHerit):
    def __init__(self, user=None,nivDanger=1,toUpdate=False):
        super().__init__(user)
        self.nivDanger = nivDanger
        self.toUpdate = toUpdate
    def increaseHP(self) :
        nbMaxPv = int((self.user.maxpv+self.nivDanger)*(1+(self.nivDanger/5)))
        self.user.maxpv = nbMaxPv
        if self.toUpdate:
            self.user.pv = nbMaxPv
            self.toUpdate=False
    def __str__(self):
        return f"Monstre|{self.nivDanger}|{self.toUpdate}"