/*Functions in C*/
#include <stdio.h>

int max_of_four(int a, int b, int c, int d){
    int MaxNumber = a;
    if(MaxNumber < b){
        MaxNumber = b;
    }
    if(MaxNumber < c){
        MaxNumber = c;
    }
    if(MaxNumber < d){
        MaxNumber = d;
    }
    return MaxNumber;
}


int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}
