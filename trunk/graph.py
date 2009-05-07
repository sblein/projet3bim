

class graph:
    
    def __init__(self,s):
        f=open(s,"r")
        self.l=f.readlines()
        self.nbBases=len(self.l)
        for i in range(self.nbBases):
            self.l[i]=self.l[i].split()
            self.l[i][0]=int(self.l[i][0])
            if len(self.l[i])>2:
                self.l[i][3]=int(self.l[i][3])
    #    self.boucle=[]
        self.longueur=[]

    def boucle_longueur(self):
        for i in range(self.nbBases):
            if len(self.l[i])>2:
                k=abs(self.l[i][3]-self.l[i][0])
                self.longueur.append([self.l[i][0],self.l[i][3],k])
     #       else:
     #           self.boucle.append(self.l[i])


#s="Appariement.txt"
#g=graph(s)
#print g.l
#g.boucle_longueur()
#print
#print g.longueur
