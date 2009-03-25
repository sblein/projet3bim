

class graph:
    
    def __init__(self,s):
        f=open(s,"r")
        self.l=f.readlines()
        self.nbBases=len(self.l)
        for i in range(self.nbBases):
            self.l[i]=self.l[i].split()
            self.l[i][1]=int(self.l[i][1])
            if len(self.l[i])>2:
                self.l[i][2]=int(self.l[i][2])
    #    self.boucle=[]
        self.longueur=[]

    def boucle_longueur(self):
        for i in range(self.nbBases):
            if len(self.l[i])>2:
                k=abs(self.l[i][2]-self.l[i][1])
                self.longueur.append([self.l[i][1],self.l[i][2],k])
     #       else:
     #           self.boucle.append(self.l[i])


s="Appariement.txt"
g=graph(s)
print g.l
g.boucle_longueur()
#print g.boucle
print
print g.longueur
