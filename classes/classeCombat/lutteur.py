from classes.classeCombat.classeHerit import classeHerit

class Lutteur(classeHerit) :
    def __init__(self,user=None,nbMartial=-1):
        super().__init__(user)
        niv = 0
        if user!=None :
            niv = user.niv
        self.martiaux = [0,4,6,6,8][niv] if nbMartial==-1 else nbMartial
        self.maxMartiaux = self.martiaux
    def __str__(self) :
        return f"Lutteur|{self.martiaux}"
    def updateMartiaux(self,nb) : 
        niv = 0
        if self.user!=None :
            niv = self.user.niv
        self.maxMartiaux = [0,4,6,6,8][niv]
        self.martiaux+=nb
        if self.martiaux>self.maxMartiaux :
            self.martiaux= self.maxMartiaux
    def levelMartial(self) :
        niv = 0
        if self.user!=None :
            niv = self.user.niv
        diff =[0,4,6,6,8][niv]- self.maxMartiaux
        self.updateMartiaux(diff)