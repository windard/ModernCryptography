#include "stdio.h"

int getDecom(int a){
    int num = 0;
    for (int i = 1; i <= a; ++i)
    {
        if(a%i==0){
            num += 1;
        }
    }
        return num;
}

int main(int argc, char const *argv[])
{
    int n = 1;
    int numsum = 0;
    while(1){
        numsum += n;
        n += 1;
        if(n>1000){
            if(getDecom(numsum)>500){
                printf("%d,%d,%d",n,numsum,getDecom(numsum));
                break;
            }
            if(n%100==0){
                printf("%d:%d\n",n,numsum );
            }
        }
    }
    return 0;
}
