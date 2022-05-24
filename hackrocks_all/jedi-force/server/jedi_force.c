#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

char* buffer[10];
int index_space = 0;

void add_jedi(){
	int candidate;
	char name[100];
	int age;

	printf("enter jedi number:\n");
	scanf("%d", &candidate);

	printf("enter jedi age: \n");
	scanf("%d", &age);

	buffer[candidate] = (char *) malloc(age);
	printf("enter jedi name:\n");
	read(0, buffer[candidate], age);
	
	index_space++;

	printf("data input success !\n");

}

void cancel_jedi(){
	int candidate;
	printf("enter jedi number to cancel:\n");
	scanf("%d", &candidate);
	free(buffer[candidate]);
	printf("free done\n");
	index_space--;
}

void show_jedi(){
	int candidate;
	printf("enter jedi number: \n");
	scanf("%d", &candidate);
	printf("jedi data: %s", buffer[candidate]);
}

int main(){
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);
  	setbuf(stderr, NULL);
	while(1){
		int menu = 0;
		printf("\nJEDI REGISTRATION\n\n1. add jedi\n2. show jedi\n3. cancel jedi\n4. exit\n\nchoose:");
		scanf("%d", &menu);
		switch(menu){
			case 1:
				add_jedi();
				break;
			case 2:
				show_jedi();
				break;
			case 3:
				cancel_jedi();
				break;

			case 4:
				exit(0);
				break;
		} // case

	}// while
	
}