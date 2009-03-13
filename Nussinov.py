# Compare deux bases et renvoie vrai si elles peuvent s'apparier, faux sinon
def Match(a,b):
    if((a[0]=="A" and b[0]=="U") or (a[0]=="U" and b[0]=="A")):
        return True
    if((a[0]=="G" and b[0]=="C") or (a[0]=="C" and b[0]=="G")):
        return True
    return False

# La classique fonction min
def min(list):
    min=list[0]
    for i in range(len(list)):
       if(min > list[i]):
           min=list[i]
    return min

# La classique fonction miax
def min(list):
    max=list[0]
    for i in range(len(list)):
       if(max < list[i]):
           max=list[i]
    return max

# Fonction d'affichage de la matrice triangulaire inferieure
def printi(mat,n):
    for i in range(1,n,1):
        list=[]
        for j in range(i):
            list.append(mat[i*(i-1)/2+j])
        print list

# Fonction d'affichage de la matrice triangulaire superieure
def prints(mat,n):
    for i in range(n):
        list=[]
        for j in range(n-i):
            list.append(mat[i*(i-1)/2+j])
        print list   

def NbLiaison(seq,k):
    nb=0
    

# Calcule la matrice inferieure suivant l'algorithme de Nussinov
def MatInf(seq):
    T=len(seq)
    mat=[]
    for i in range(T*(T-1)/2):
        mat.append(0)

    for j in range(1,T,1):
        for i in range(0,j,1):
            list=[]
            for k in range(i,j+1,1):
                list.append(seq[k])

            nbA=list.count("A")
            nbU=list.count("U")
            nbC=list.count("C")
            nbG=list.count("G")
            l1=[nbA,nbU]
            l2=[nbC,nbG]
            mat[j*(j-1)/2+i]=min(l1)+min(l2)            
    return mat            
                

def MatSup(seq):
    T=len(seq)
    
    list=[]
    for k in range(1,T,1):
        seqi=[]
        seqs=[]
        for i in range(k):
            seqi.append(seq[i])
        for i in range(k+1,T,1):
            seqs.append(seq[i])
        print seqi,seqs
        mati=MatInf(seqi)
        printi(mati,len(mati))
        mats=MatInf(seqs)
        printi(mats,len(mats))
        #list.append(mati[(len(seqi)-1)*(len(seqi)-2)/2])
    #m=max(list)
    return 21#list.index(m)

        


#################
#               #
# Zone de tests #
#               #
#################

f=open("Sequence1.txt","r")
seq=f.readline()
print seq
printi(MatInf(seq),len(seq))
#print MatInf(seq)
#print MatSup(seq)
#prints(MatInf(seq),10)
