/*Playing with Characters*/
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#define MAX_LEN 100

int main() 
{
    char ch, s[MAX_LEN], sen[MAX_LEN]; 
    scanf("%c", &ch);
    scanf("%s", s);
    scanf("\n");
    fgets(sen, MAX_LEN, stdin);
    printf("%c", ch);
    printf("\n%s", s);
    printf("\n%s", sen);
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}
