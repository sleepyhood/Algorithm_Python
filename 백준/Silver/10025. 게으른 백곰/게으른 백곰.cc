#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
using namespace std;

#define ICE 1000000
#define ARM 2000000

// 얼음좌표: i(0 ≤ xi ≤ 1,000,000)
// 팔 길이: K(1 ≤ K ≤ 2,000,000)
int main()
{
	long long n, k;
	// n개의 지점에 한 팔의길이 k
	cin >> n >> k;

	// 얼음양, 좌표(0부터 시작함 주의)
	long long maxIdx = 0;
	long long* iceArr = new long long[ICE + 1];
	long long* coordArr = new long long[ICE + 1];

	// n 개 입력받은 얼음값과 얼음 위치 
	for (long long i = 0; i < n; i++) {
		long long g, x;

		cin >> g >> x;
		if (maxIdx < x) { // 최대 좌표 갱신
			maxIdx = x;
		}
		iceArr[i] = g;
		coordArr[i] = x;
	}

	// 좌표별 얼음(인덱스 0에서 maxIdx까지만)
	// 최대 좌표위치까지만 돌도록 설정
	long long* arr = new long long[maxIdx + 1]{ 0 };
	// 배열 내부값을 인덱스로 사용하므로 n번 반복
	for (long long i = 0; i < n ; i++) {
		arr[coordArr[i]] = iceArr[i];
	}

	long long sum = 0;
	// 이전 슬라이딩 도어와 거의 유사


	// 팔의 길이는 얼음의 위치를 초과할 수 있음 
	/*if (k / 2 > maxIdx) {
		for (long long i = 0; i < maxIdx; i++)
			sum += arr[i];
		cout << sum << endl;
		return 0;
	}*/

	for (long long i = 0; i < (k * 2) + 1 ; i++) {
		if (i > maxIdx)	// 만약 현재 더 이상 더할 수 없다면 탈출 (인덱스 초과 방지)
			break;
		sum += arr[i];
	}
	long long ans = sum;

	// 주의: 구간의 길이는 K*2가 아닌 k*2+1
	for (long long i = k + 1; i < maxIdx - k; i++) {
		if (i > maxIdx) // 만약 현재 더 이상 더할 수 없다면 탈출 (인덱스 초과 방지)
			break;

		if (i - k - 1 >= 0)
			sum -= arr[i - k - 1];
		if (i + k < maxIdx)
			sum += arr[i + k];

		//cout<<"i-k-1: " <<i-k-1 << "\t" << "i+k-1: " << i+k-1 << endl;
		ans = max(sum, ans);

	}
	cout << ans << endl;
	// 실질적으로 팔의 길이가 최대좌표보다 길다면 이미 sum으로 답이 나온다.
	return 0;
}