#include<stdio.h>
#include<malloc.h>
#include<sys/types.h>
#include<unistd.h>

void * old_malloc_hook;
void * old_free_hook;

static void my_init_hook (void);
static void * my_malloc_hook (size_t, const void *);
static void * my_free_hook (void*, const void *);

static void my_init (void){
  old_malloc_hook = __malloc_hook;
  old_free_hook = __free_hook;
  __malloc_hook = my_malloc_hook;
  __free_hook = my_free_hook;
}

static void * my_malloc_hook (size_t size, const void *caller){
  void *result;
  /* Restore all old hooks */
  __malloc_hook = old_malloc_hook;
  __free_hook = old_free_hook;
  /* Call recursively */
  result = malloc (size);
  /* Save underlying hooks */
  old_malloc_hook = __malloc_hook;
  old_free_hook = __free_hook;
  /* printf might call malloc, so protect it too. */
  printf ("malloc (%u) returns %p\n", (unsigned int) size, result);
  /* Restore our own hooks */
  __malloc_hook = my_malloc_hook;
  __free_hook = my_free_hook;
  return result;
}

static void * my_free_hook (void *ptr, const void *caller) {
  /* Restore all old hooks */
  __malloc_hook = old_malloc_hook;
  __free_hook = old_free_hook;
  /* Call recursively */
  free (ptr);
  /* Save underlying hooks */
  old_malloc_hook = __malloc_hook;
  old_free_hook = __free_hook;
  /* printf might call free, so protect it too. */
  printf ("freed pointer %p from %p\n", ptr, caller);
  /* Restore our own hooks */
  __malloc_hook = my_malloc_hook;
  __free_hook = my_free_hook;
}


int main(){
    my_init();

    pid_t pid = getpid();
    printf("pid: %lu\n", pid);

    getchar();

    char* a = malloc(0x20);
    char* b = malloc(0x20);
    char* c = malloc(0x20);
    strcpy(a,"aaaahello world!aaaa");
    strcpy(b,"aaaabbbbccccddddeeeeffffgggghhhh");
    strcpy(c,"11112222333344445555666677778888");

    printf("my_hook at %p\n",my_malloc_hook);
    printf("hook: %p\nhook location: %p\n",*__malloc_hook,&__malloc_hook);
    

    free(b);
    free(c);
    free(a);

    c = malloc(0x20);
    b = malloc(0x20);
    a = malloc(0x20);
    
    return 0;

}

