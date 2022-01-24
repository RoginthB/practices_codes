#include <stdio.h>
void findDaysInAMonth();
int main()
{
   int n;
    scanf("%d",&n);
    for (int i=0;i<n;i++){
        for (int j=0;j<n;j++){
            if(  j==0 || j==n-1 || (i==j && i<=n/2  )||(j==n-i-1 && j>=n/2-1))
            printf("*");
            else
            printf(" ");
        }
        printf("\n");
    } 
printf("find day in a month ");

findDaysInAMonth();
    return 0;
}
void maxAndMin()
{
    int max1 = 0, max2 = 0, max3 = 0, min1 = 99999, min2 = 99999, min3 = 99999, n;
    printf("enter the n value : ");
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        int x;
        printf(">>> ");
        scanf("%d", &x);
        if (x > max3)
        {
            int y=max3;
            max3 = x;
            min3=y;
            if (max3 > max2)
            {
                int y = max2;
                max2 = max3;
                max3 = y;
                if (max2 > max1)
                {
                    int y = max1;
                    max1 = max2;
                    max2 = y;
                }
            }
        }
        else
        {
            if (x < min3)
            {
                min3 = x;
                if (min3 < min2)
                {
                    int y = min2;
                    min2 = min3;
                    min3 = y;
                    if (min2 < min1)
                    {
                        int y = min1;
                        min1 = min2;
                        min2 = y;
                    }
                }
            }
        }
    }
    printf("%d,%d,%d\n", max1, max2, max3);
    printf("%d,%d,%d", min1, min2, min3);
}

void findDaysInAMonth()
{
    int input;
    printf("enter the input : ");
    scanf("%d",&input);
    int mounthDays[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}, year, mounth;
    year = input / 100;
    mounth = input % 100;
    if (year % 100 == 0)
    {
        if (year % 400 == 0)
        {
            if (mounth == 2)
            {
                printf("%d", (mounthDays[mounth - 1] + 1));
            }
            else
            {
                printf("%d", mounthDays[mounth - 1]);
            }
        }
    }
    else if (year % 4 == 0)
    
    {
        if (mounth == 2)
        {
            printf("%d", (mounthDays[mounth - 1] + 1));
        }
        else
        {
            printf("%d", mounthDays[mounth - 1]);
        }
    }
    else
    {
        printf("%d", mounthDays[mounth - 1]);
    }
    
}

