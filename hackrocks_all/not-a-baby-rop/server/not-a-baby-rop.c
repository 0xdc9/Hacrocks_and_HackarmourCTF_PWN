#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>


void warm_up(){
	char buffer[128];
	scanf("%s", buffer);
}

int main(){
	puts("let's see what u got");
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);
  	setbuf(stderr, NULL);
  	warm_up();

}