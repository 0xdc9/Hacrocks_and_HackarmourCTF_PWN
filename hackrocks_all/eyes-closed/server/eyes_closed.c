#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(){
	char buffer[32];
	char feedback[300];
	printf("close your eyes and imagine something\n");
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);
  	setbuf(stderr, NULL);
  	printf("tell me, what did you see?: \n");
  	scanf("%s", buffer);
  	printf("a ");
  	printf(buffer);
  	printf(" ?nice one\n");

  	printf("please, give me a feedback: \n");
  	scanf("%s", feedback);

  	printf("thanks, see you later\n");
}