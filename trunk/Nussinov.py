import numpy

# Matrice de score des appariements possibles
def Match2(a,b):
    if((a[0]=="A" and b[0]=="U") or (a[0]=="U" and b[0]=="A")):
        return -3
    elif((a[0]=="G" and b[0]=="C") or (a[0]=="C" and b[0]=="G")):
        return -4
    elif((a[0]=="G" and b[0]=="U") or (a[0]=="U" and b[0]=="G")):  
    	return -2    
    else:
    	return 0

# La classique fonction min
def min(list):
    min=list[0]
    for i in range(len(list)):
       if(list[i]<min):
           min=list[i]
    return min

# La classique fonction max
def max(list):
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

def Match(seq):
	nbA=seq.count("A")
	nbU=seq.count("U")
	nbC=seq.count("C")
	nbG=seq.count("G")
	nb=min([nbA,nbU])*Match2("A","U")+min([nbG,nbC])*Match2("G","C")
	return nb
    

# Calcule la matrice inferieure suivant l'algorithme de Nussinov
def Mat(seq):
	T=len(seq)
	mat=numpy.zeros(T*T)
	mat=numpy.reshape(mat,(T,T))
	
	for p in range(1,T,1):
		if p==1:
			for j in range(1,T,1):
				mat[j-1,j]=Match2(seq[j-1],seq[j])		
		else :
			for j in range(p,T,1):
				#mat[j-p,j]=Match(seq[j-p:j+1])
				A=mat[j-p,j-1]
				B=mat[j-p+1,j]
				C=Match2(seq[j-p],seq[j])+mat[j-p+1,j-1]
				list=[]
				for k in range(j-p+1,j,1):
					list.append(mat[j-p,k]+mat[k+1,j])
				D=min(list)
				mat[j-p,j]=min([A,B,C,D])
				#print "p=%d \t j=%d %s\t "%(p+1,j,seq[j-p:j+1])
	return mat
	
def TraceBack(mat,T,seq):		
	way=[]
	way.append([0,T-1,mat[0,T-1]])
	#if(mat[0,T-1]==mat[0,T-2] or mat[0,T-1]==mat[1,T-1]):
		#way.pop()
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
                    way.append([i+kl+1,j,mat[i+kl+1,j]])
                    i+=kl+1
	return way

def Transfo(u,v):
	if(u[0]==v[0] and u[1]==(v[1]+1)):
		return "A"
	elif(u[0]==(v[0]-1) and u[1]==v[1]):
		return "B"
	elif(u[0]==(v[0]-1) and u[1]==(v[1]+1)):
		return "C"
	else:
		return "D"

def BasePairs(seq,way):		
	bp=[]
	for i in range(len(way)-1):
		t=Transfo(way[i],way[i+1])
		#print t,way[i]
		if(t=="A"):
			bp.append([way[i][1],seq[way[i][1]]])
		elif(t=="B"):
			bp.append([way[i][0],seq[way[i][0]]])
		elif(t=="C"):
			bp.append([way[i][1],seq[way[i][1]],way[i][0],seq[way[i][0]]])
		#elif(t=="D"):
			#bp.append([way[i][1],seq[way[i][1]],way[i][0],seq[way[i][0]]])
	return bp	
			
		
#################
#               #
# Zone de tests #
#               #
#################

f=open("Sequence3.txt","r")
seq=f.readline()
seq=seq.rstrip('\n')
print seq
print Mat(seq)
print TraceBack(Mat(seq),len(seq),seq)
print BasePairs(seq,TraceBack(Mat(seq),len(seq),seq))
