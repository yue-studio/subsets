#bitmask method in C

#include <stdio.h>

void subset(int *nums, int comb) {
    for (int i = 0; i < 16; i++ ) {
        if (comb & (1u << i)) {
           printf("%d", nums[i]);
        }
    }
    printf("\n");
}

int main()
{
    int numlist[] ={1, 2, 3};
    size_t n = sizeof(numlist)/sizeof(numlist[0]);
    int noSubsets = (int) pow((double) 2, n);

    for (int i=1; i< noSubsets;i++) {
         subset(numlist, i);
    }

    return 0;
}
