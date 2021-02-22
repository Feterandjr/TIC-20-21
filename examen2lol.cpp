#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
	int cont;
	char pala1[10];
	int long1;
	char pala2[10];
	int long2;
	char pala3[10];
	int long3;
	char pala4[10];
	int long4;
	char pala5[10];
	int long5;
	printf("Escriba la primera palabra: ");
	scanf("%s",pala1);
	for (long1=strlen(pala1);long1>10;){
	if (long1>10){
		printf("Escriba la palabra,tiene que tner no mas de 10 letras: ");
		scanf("%s",pala1);
		long1=strlen(pala1);
	}
	}
	printf("Escriba la segunda palabra: ");
	scanf("%s",pala2);
	for (long2=strlen(pala2);long2>10;){
	if (long2>10){
		printf("Escriba la palabra,tiene que tner no mas de 10 letras: ");
		scanf("%s",pala2);
		long2=strlen(pala2);
	}
	}
	printf("Escriba la tercera palabra: ");
	scanf("%s",pala3);
	for (long3=strlen(pala3);long3>10;){
	if (long3>10){
		printf("Escriba la palabra,tiene que tner no mas de 10 letras: ");
		scanf("%s",pala3);
		long3=strlen(pala3);
	}
	}
	printf("Escriba la cuarta palabra: ");
	scanf("%s",pala4);
	for (long4=strlen(pala4);long4>10;){
	if (long4>10){
		printf("Escriba la palabra,tiene que tner no mas de 10 letras: ");
		scanf("%s",pala4);
		long1=strlen(pala4);
	}
	}
	printf("Escriba la quinta palabra: ");
	scanf("%s",pala5);
	for (long5=strlen(pala5);long5>10;){
	if (long5>10){
		printf("Escriba la palabra,tiene que tner no mas de 10 letras: ");
		scanf("%s",pala5);
		long1=strlen(pala5);
	}
}

	return 0;
}
