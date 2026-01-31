#include <pthread.h>
#include <unistd.h>
#include <stdio.h>

void* myturn(void * arg){
    for(int i = 0; i<8; i++){
        sleep(1);
        printf("My Turn!\n");
    }
    return NULL;
}

void yourturn(){
    for(int i = 0; i<3; i++){
        sleep(1);
        printf("Your Turn!\n");
    }
}

int main(){
    pthread_t newthread;
    pthread_create(&newthread,NULL,myturn,NULL);
    //myturn();
    yourturn();
    pthread_join(newthread, NULL); // wait the main thread until other threads finishes
}