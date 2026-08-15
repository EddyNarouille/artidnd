from classes.classeCombat.classeHerit import classeHerit

class SangMele(classeHerit) :
    def __init__(self,dieuBonus="Zeus",dieuMalus="Arès",user = None):
        self.dieuBonus = dieuBonus
        self.dieuMalus = dieuMalus
        super().__init__(user)
    def __str__(self):
        return f"Sang-mêlé / {self.dieuBonus} / {self.dieuMalus}"