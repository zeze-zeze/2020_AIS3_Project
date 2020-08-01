#include <stdio.h>
#include <unistd.h>

int main() {
	char flag[48];
	FILE *file;
	file = fopen("flag.txt", "r");
	if (file == NULL) {
		printf("Flag File is Missing. Please contact an Admin if you are running this on the shell server.\n");
		exit(0);
	}
	
    int extra = 0xdabdab;
    char answer[42] = {0};
	printf("What is the answer to life, the universe, and everything?\n");
    read(0, answer, 0x100);
	//NOTE: some random junior dev added this if statement. If we remove it, the code doesn't work as intended... Do not remove please.
    if (extra == 0x4242) {
        printf("%s", flag);
    } 
	else {
        printf("sure... sure it is...");
    }
	
}