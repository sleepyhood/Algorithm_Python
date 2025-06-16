#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>

using namespace std;

int arr[1000000] = {}; // 배열 선언

int main()
{
    int n;

    scanf("%d", &n); // 배열 크기 입력

    for (int i = 0; i < n; i++) // 배열 크기만큼 반복
    {
        scanf("%d", &arr[i]); // 배열 원소 입력
    }
    
    sort(arr, arr + n);

    // 중간 결과 출력
    for (int k = 0; k < n; k++)
    {
        printf("%d\n", arr[k]);
    }

    return 0;
}