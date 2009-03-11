#include <sdtdio.h>
#include <stdlib.h>

int Matching(char a,char b)
{
    if((a=="A" && b=="U") || (a=="U" and b=="A")) return 1;
    if((a=="G" && b=="C") || (a=="C" and b=="G")) return 1;
    return 0;					      
}

int * Nussi(char* seq,int N)
{
    int * res=(int*)malloc(N*(N+1)/2*sizeof(int));
    int i,j,p=0;
    for(p=1;p<N;p++)
    {
	for(j=1;j<N;j++)
	{
	    for(i=0;i<j && (j-i)==9;i++)
	    {
		for(k=i;k<j;k++)
		{
		    cpt=0;
		    if(Matching(char[i+k],char[j])==1)
		    {
			cpt++;
		    }
		    res[j*(j-1)/2+i]=cpt;
		}
	    }
	}
    }
    return res;
}

int main(void)
{
    seq="CGCCGCGCCG";
    mat=Nussi(seq,10);
    int i,j;
    for(j=0;j<10;j++)
    {
	for(i=0;i<j;i++)
	{
	    printf("%d ",mat[j*(j-1)/2+i]);
	}
	printf("\n");
    }
    return 0;
}
