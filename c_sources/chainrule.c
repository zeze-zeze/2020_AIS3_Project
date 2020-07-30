#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdbool.h>

#define BUFSIZE 16

int passCode;

void getPass(){
	printf("%d",passCode);
}

void setPass(unsigned int code) {
  passCode = code;
}

void passCheck() {
  char flag[48];
  FILE *file;
  file = fopen("flag.txt", "r");
  if (file == NULL) {
    printf("Flag File is Missing. Please contact an Admin if you are running this on the shell server.\n");
    exit(0);
  }

  fgets(flag, sizeof(flag), file);

  if (passCode = 0xDABDAB) {
    printf("%s", flag);
    return;
  }
  else {
    printf("You won't get the flag that easily..\n");
  }
}

void run() {
  char buf[16];
  printf("What is your favorite example of a Markov chain?\nEnter your input: ");
  return gets(buf);
}

int main(int argc, char **argv){
  setvbuf(stdout, NULL, _IONBF, 0);
  gid_t gid = getegid();
  setresgid(gid, gid, gid);
  run();
}
