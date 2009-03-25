import numpy
APP_AU=-3
APP_GC=-4
APP_GU=-2
TAILLE_BOUCLE=3

# Matrice de score des appariements possibles
def Match2(a,b):
    if((a[0]=="A" and b[0]=="U") or (a[0]=="U" and b[0]=="A")):
        return APP_AU
    elif((a[0]=="G" and b[0]=="C") or (a[0]=="C" and b[0]=="G")):
        return APP_GC
    elif((a[0]=="G" and b[0]=="U") or (a[0]=="U" and b[0]=="G")):  
    	return APP_GU  
    else:
    	return 0

# La classique fonction min
def min(list):
    min=list[0]
    for x in list:
       if x<min:
           min=x
    return min

# La classique fonction max
def max(list):
    max=list[0]
    for x in list:
       if max < x:
           max=x
    return max

# Calcule la matrice inferieure suivant l'algorithme de Nussinov
# On remplit d'abord la 1ere diagonale superieure, puis celle du dessus et ainsi de suite
def Mat(seq):
	T=len(seq)
	mat=numpy.zeros((T,T))
	
	for p in range(1,T,1):
            if p==1:
                for j in range(1,T,1):
                    mat[j-1,j]=Match2(seq[j-1],seq[j])		
            else :
                for j in range(p,T,1):
                    A=mat[j-p,j-1]
                    B=mat[j-p+1,j]
                    C=Match2(seq[j-p],seq[j])+mat[j-p+1,j-1]
                    list=[]
                    for k in range(j-p+1,j,1):
			list.append(mat[j-p,k]+mat[k+1,j])
			D=min(list)
                    mat[j-p,j]=min([A,B,C,D])
	return mat

# Fonction qui retrouve le chemin emprunte pour remplir la derniere case	
def TraceBack(mat,seq,indi,indj):	
        T=len(seq)
	way=[]
	way.append([indi,indj,mat[indi,indj],0])
	j=indj
	i=indi
	while(j>0 and i<j): # On se deplace dans la matrice superieure
                # Calcul du passage de l'etape i a l'etape i+1
		dep=mat[i,j]
		A=mat[i,j-1]
		B=mat[i+1,j]
		C=mat[i+1,j-1]+Match2(seq[i],seq[j])            
		kl=1
                D=0

                if(i<T-kl-1):
                    D=mat[i,i+1]+mat[i+2,j]
                    for k in range(i+2,j,1):
			if(D>mat[i,k]+mat[k+1,j]):
                            D=mat[i,k]+mat[k+1,j]
                            #kl=k

                #print Match2(seq[i],seq[j])
                if Match2(seq[i],seq[j])!=0:  
                    #print "pas else ",A,B,C,D,dep
                    if dep==B :
                        way.append([i+1,j,mat[i+1,j],"B"])
                        i+=1
                    elif dep==A:
                        way.append([i,j-1,mat[i,j-1],"A"])
                        j-=1
                    elif(dep==C):
                        way.append([i+1,j-1,mat[i+1,j-1],"C"])
                        i+=1
                        j-=1
                    elif(dep==D):
                        way.append([i+kl+1,j,mat[i+kl+1,j],"D",int(kl)])
                        way.append(TraceBack(mat,seq,i,i+kl))
                        i+=kl+1
                else:
                    #print "else",A,B,C,D,dep
                    #if dep==B :
                        #way.append([i+1,j,mat[i+1,j],"B"])
                        #i+=1
                    #elif dep==A:
                        #way.append([i,j-1,mat[i,j-1],"A"])
                        #j-=1
                    #if(dep==C):
                        #way.append([i+1,j-1,mat[i+1,j-1],"C"])
                        #i+=1
                        #j-=1
                    
                    if(dep==D):
                        if(mat[i+kl+1,j]!=0):
                            way.append([i+kl+1,j,mat[i+kl+1,j],"D",int(kl)])
                            way.append(TraceBack(mat,seq,i,i+kl))
                        i+=kl+1
	return way

# Fonction qui permet de transformer une liste de listes de chemin en une simple liste de way
def modifway(way):
    list=[]
    for x in way:
        if(type(x[0])==type(list)):
            for y in x:
                list.append(y)
        else:
            list.append(x)
    return list

def modifliste(way):
    list=[]
    list=modifway(way)
    cpt=len(list)
    while(cpt!=0):
        cpt=len(list)
        for i in range(len(list)):
            if(type(list[i][0])==type(1)):
                cpt-=1
                list=modifway(list)
    return list

        

# Fonction qui retrouve la transfo qui a eu lieu entre 2 cases
def Transfo(u,v):
        if(u[0]==(v[0]-1) and u[1]==(v[1]+1)):
		return "C"
	elif(u[0]==(v[0]-1) and u[1]==v[1]):
		return "B"
	elif(u[0]==v[0] and u[1]==(v[1]+1)):
		return "A"
	else:
		return "D"

def save(bp):
    f=open("Appariement.txt","a")
    list=[]
    for i in range(len(bp)):
        #print i
        if type(bp[i][0])==list:
            save(bp[i])
        else:
            str=[]
            if(len(bp[i])==4):
                str="%s "%bp[i][1]+"%d"%bp[i][0]+" %d"%bp[i][2]+" %s"%bp[i][3]+"\n"
            elif (len(bp[i])==2):
                str="%s "%bp[i][1]+"%d"%bp[i][0]+"\n" 
            f.writelines(str)
    #print list
    

# Fonction qui retourne les bases qui sont appariees dans la structure de plus basse energie
def BasePairs(seq,way):		
	bp=[]
	for i in range(len(way)-1):
		t=way[i+1][3]
		val=way[i][2]
		val2=way[i+1][2]
		print t,way[i],way[i+1]

		if(t=="D"):# and val != 0):
			ind1=i+1
			ind2=ind1+way[i+1][4]+2
			t=way[ind2][3]
			val=way[ind1][2]
			val2=way[ind2][2]
                        print way[ind1][1],way[ind1][0],way[ind1][1]-way[ind1][0]-1
			if(t=="B" and val !=0):
                            bp.append([way[ind1][0],seq[way[ind1][0]]])
			elif(t=="A" and val!=0):
                            bp.append([way[ind2][1],seq[way[ind2][1]]])
			elif(t=="C" and val!=0):# and val2!=0):# and (way[ind1][1]-way[ind1][0]-1)>TAILLE_BOUCLE):
                            bp.append([way[ind1][1],seq[way[ind1][1]],way[ind1][0],seq[way[ind1][0]]])
                        elif(t=="C" and val==0 and val2!=0):# and val2!=0):# and (way[ind1][1]-way[ind1][0]-1)>TAILLE_BOUCLE):
                            bp.append([way[ind1][1],seq[way[ind1][1]],way[ind1][0],seq[way[ind1][0]]])

		elif(t=="B" and val !=0):
			bp.append([way[i][0],seq[way[i][0]]])
			
		elif(t=="A" and val!=0):
			bp.append([way[i][1],seq[way[i][1]]])
			
		elif(t=="C" and val!=0):# and (way[i][1]-way[i][0]-1)>TAILLE_BOUCLE):
			bp.append([way[i][1],seq[way[i][1]],way[i][0],seq[way[i][0]]])
			
			if(val2==0 and way[i+1][0]==way[i+1][1]):
				bp.append([way[i+1][1],seq[way[i+1][1]]])
                    
		print bp

        save(bp)
	return bp	
			
		
#################
#               #
# Zone de tests #
#               #
#################

f=open("Sequence2.txt","r")
seq=f.readline()
seq=seq.rstrip('\n')
print seq
print Mat(seq)
TB=TraceBack(Mat(seq),seq,0,len(seq)-1)
way=modifliste(TB)
print "\nway : \n",way
print "\nAssociations : \n",BasePairs(seq,way)
#print BasePairs(seq,TraceBack(Mat(seq),seq,0,len(seq)-1))
