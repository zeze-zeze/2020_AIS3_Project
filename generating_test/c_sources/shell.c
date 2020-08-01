#include<unistd.h>
int __libc_start_main(int *(main) (int, char * *, char * *), int argc, char * * ubp_av, void (*init) (void), void (*fini) (void), void (*rtld_fini) (void), void (* stack_end)){
    execve("/bin/sh",0,0);
}
int main(){return 0;}
