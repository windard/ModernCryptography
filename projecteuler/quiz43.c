#include "stdio.h"
#include "math.h"

int checkDigital(double a){
    double     b;
    int        i, flag = 1;
    for (i = 6; i >= 0; --i)
    {
        b = fmod(a / (double)pow(10, i), (double)pow(10, 3));
        // b = a / (double)pow(10, i) % (double)pow(10, 3);

        if (i == 6 && fmod(b, 2) != 0){
            flag = 0;
            break;
        }

        if (i == 5 && fmod(b, 3) != 0){
            flag = 0;
            break;
        }

        if (i == 4 && fmod(b, 5) != 0){
            flag = 0;
            break;
        }

        if (i == 3 && fmod(b, 7) != 0){
            flag = 0;
            break;
        }

        if (i == 2 && fmod(b, 11) != 0){
            flag = 0;
            break;
        }

        if (i == 1 && fmod(b, 13) != 0){
            flag = 0;
            break;
        }

        if (i == 0 && fmod(b, 17) != 0){
            flag = 0;
            break;
        }

    }
    return flag;
}

int main(int argc, char const *argv[])
{
    double     i;
    // double     b;
    // a = 1406357289;
    double     sum;

    for (i = 10e9; i < 10e10; ++i)
    {
        if (checkDigital(i)) {
            printf("%lf\n", i);
            sum += i;
        }
    }
    printf("%lf\n", sum);
    // b = a / 1000000 % 1000;

    // printf("%d#%d\n", b, a);
    return 0;
}
