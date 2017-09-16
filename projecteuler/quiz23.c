#include "stdio.h"


int DecomSum(int a){
    int num = 0;
    for (int i = 1; i < a; ++i)
    {
        if(a%i==0){
            num += i;
        }
    }
        return num;
}

int checkAbundantSum(int n){
    for (int j = 0; j < (n/2 + 1); ++j)
    {
        if (DecomSum(j) > j && DecomSum(n-j) > n-j)
        {
            return 1;
        }
    }
    return 0;
}

int solve(int n){
    int sum = 0;
    for (int i = 0; i < n; ++i)
    {
        if(!checkAbundantSum(i)){
            sum += i;
        }
    }
    return sum;
}
// def check_abundant_sum(n):
//     for i in xrange(n):
//         for x in xrange(i/2 + 1):
//             if is_abundant(x) and is_abundant(i-x):
//                 sum_all.append(i)
//                 break

// check_abundant_sum(10000)
// print sum_all
// print set(xrange(10000)).difference(set(sum_all))
// print sum(set(xrange(10000)).difference(set(sum_all)))

int main(int argc, char const *argv[])
{
    printf("%d\n", solve(28123));
    // 4179871
    // printf("%d\n", 12/2);
    // printf("%d\n", 13/2);
    // for (int i = 0; i < 100; ++i)
    // {
    //     if (DecomSum(i) > i){
    //         printf("%d ", i);
    //     }
    // }
    return 0;
}