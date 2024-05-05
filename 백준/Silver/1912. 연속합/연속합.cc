#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    // 수를 최대 연속하여 1~n개 만큼 선택할 수 있다.
    // 이전 사탕문제와 달리, 몇개를 가져가는지는 정해져있지 않음
    // 1000ms는 시간복잡도 최대 O(nlogn) 이하여야함
    long long n;
    cin >> n;

    long * arr = new long [n] {0};
    long * sumArr = new long [n] { 0 };

    for (long  i = 0; i < n; i++)
        cin >> arr[i];

    // 누적합 0번지는 동일
    // 기존 누적합과 달리, 최대값만 저장해서 기억하여 저장하면된다.
    // 즉, 무조건 누적하지 않고 비교후 누적하는 방식
    sumArr[0] = arr[0];
    long ans = arr[0];
    for (long  i = 1; i < n; ++i) {
        sumArr[i] = max(arr[i] + sumArr[i - 1], arr[i]);
        // 원본 배열값과 더한값이랑만 비교를 하기 때문에, 마지막 값이 무조건적으로 최대값이라는 보장은 없다. (음수도 있으므로)
        ans = max(sumArr[i], ans);
        // 때문에 돌면서 최대값을 따로 구해줘야함
    }

    /*for (long i = 0; i < n; ++i) {
        cout << sumArr[i] << " ";
    }
    cout << "\n";*/

    cout << ans<< "\n";
    return 0;
}