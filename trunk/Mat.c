#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int Matching(char a,char b)
{
  if((strcmp(&a,"A") && strcmp(&b,"U")) ||(strcmp(&b,"A") && strcmp(&a,"U"))) 
    {
      return 1;
    }
  else
    {  
      if((strcmp(&a,"G") && strcmp(&b,"C")) ||(strcmp(&b,"G") && strcmp(&a,"C"))) 
	{
	  return 1;
	}
	else
	  {
	    return 0;
	  }
    }					      
}

int * Nussi(char* seq,int N)
{
    int * res=(int*)malloc(N*(N-1)/2*sizeof(int));
    int i,j,p,k=0;

    for(i=0;i<N*(N-1)/2;i++) 
      {
	res[i]=0;
      }

    p=1; /* On attend avant de boucler */
    for(j=1;j<N;j++)
      {
	for(i=0;i<j;i++)
	  {
	    if(j-i==p)
	      {
		int cpt=0;
		if(Matching(seq[i],seq[j])==1)
		  {
		    printf(&seq[i]);
		    printf("\n");
		    printf(&seq[j]);
		    printf("\n");
		    cpt++;		    
		  }

		if(cpt!=0)
		  {
		    printf("%d %d\n",j*(j-1)/2+i,cpt);
		    res[j*(j-1)/2+i]+=cpt;
		  }
	      }	      
	  }
      }

    return res;
}

int main(void)
{
    char *seq="CGCCGCGCCG";
    int * mat=Nussi(seq,10);
    int i,j;
    printf(seq);
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
