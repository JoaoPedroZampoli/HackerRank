/*Pointers in C*/
#include <stdio.h>

void update(int *a,int *b) {
    int pa = *a, pb = *b;
    *a = pa + pb;
    *b = pa - pb;
    if(*b < 0){
        *b *= -1;
    }
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
