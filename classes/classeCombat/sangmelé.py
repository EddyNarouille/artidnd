from classes.classeCombat.classeHerit import classeHerit

class SangMele(classeHerit) :
    def __init__(self,dieuBonus="Zeus",dieuMalus="Ares"):
        self.dieuBonus = dieuBonus
        self.dieuMalus = dieuMalus
    def __str__(self):
        return f"Sang-mélé / {self.dieuBonus} / {self.dieuMalus}"