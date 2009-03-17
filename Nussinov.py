import numpy
APP_AU=-3
APP_GC=-4
APP_GU=-2

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
       if(x<min):
           min=x
    return min

# La classique fonction max
def max(list):
    max=list[0]
    for x in list:
       if(max < x):
           max=x
    return max

# Calcule la matrice inferieure suivant l'algorithme de Nussinov
def Mat(seq):
	T=len(seq)
	mat=numpy.zeros((T,T))
	#mat=numpy.reshape(mat,(T,T))
	
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
def TraceBack(mat,seq):	
        T=len(seq)
	way=[]
	way.append([0,T-1,mat[0,T-1]])
	j=T-1
	i=0
	while(j>0 and i<j):
		dep=mat[i,j]
		A=mat[i,j-1]
		B=mat[i+1,j]
		C=mat[i+1,j-1]+Match2(seq[i],seq[j])
		kl=1
                D=0
                if(i<T-2):
                    D=mat[i,i+1]+mat[i+2,j]
                    for k in range(i+2,j,1):
			if(D>mat[i,k]+mat[k+1,j]):
				D=mat[i,k]+mat[k+1,j]
				kl=k
                if dep==A:
                    way.append([i,j-1,mat[i,j-1]])
                    j-=1
		elif dep==B :
                    way.append([i+1,j,mat[i+1,j]])
                    i+=1
		elif(dep==C):
                    way.append([i+1,j-1,mat[i+1,j-1]])
                    i+=1
                    j-=1
		elif(dep==D):
                    way.append([i+kl+1,j,mat[i+kl+1,j],int(kl)])
                    i+=kl+1
	return way

# Fonction qui retrouve la transfo qui a eu lieu entre 2 cases
def Transfo(u,v):
	if(u[0]==v[0] and u[1]==(v[1]+1)):
		return "A"
	elif(u[0]==(v[0]-1) and u[1]==v[1]):
		return "B"
	elif(u[0]==(v[0]-1) and u[1]==(v[1]+1)):
		return "C"
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
		t=Transfo(way[i],way[i+1])
                print t
		if(t=="A"):
                    bp.append([way[i][1],seq[way[i][1]]])
		elif(t=="B"):
                    bp.append([way[i][0],seq[way[i][0]]])
		elif(t=="C"):
                    bp.append([way[i][1],seq[way[i][1]],way[i][0],seq[way[i][0]]])
		elif(t=="D"):
                    seq2=[]
                    for j in range(way[i+1][3]+1):
                        seq2.append(seq[j])
                    print way[i+1][3],seq2
                    if(len(seq)>0):
                        bp.append(BasePairs(seq2,TraceBack(Mat(seq2),seq2)))
        save(bp)
	return bp	
			
		
#################
#               #
# Zone de tests #
#               #
#################

f=open("Sequence1.txt","r")
seq=f.readline()
seq=seq.rstrip('\n')
print seq
print Mat(seq)
print TraceBack(Mat(seq),seq)
print BasePairs(seq,TraceBack(Mat(seq),seq))
