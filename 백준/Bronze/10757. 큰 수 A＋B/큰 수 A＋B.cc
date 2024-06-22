#define _CRT_SECURE_NO_WARNINGS
#define MAX 100001
#include <iostream>
#include <string> //need this

using namespace std;

/*
    기초미적분, 이산수학, 선형대수학, 컴파일러, C, Python, JAVA, 자료구조

    컴퓨터네트워크, 운영체제,

*/

int a[MAX];
int b[MAX];
int res[MAX];

int main()
{
    string s1, s2;
    cin >> s1 >> s2;

    int idx = MAX - 1;

    for (int i = s1.length() - 1; i >= 0; i--) {
        a[idx] = (int)(s1[i] - '0');
        idx--;
    }

    idx = MAX - 1;
    for (int i = s2.length() - 1; i >= 0; i--) {
        b[idx] = (int)(s2[i] - '0');
        idx--;
    }

    idx = MAX - 1;

    int maxLen;

    /*for (int i = MAX - s1.length(); i < MAX; i++) {
        cout << a[i];
    }
    cout << "\n";
    for (int i = MAX - s2.length(); i < MAX; i++) {
        cout << b[i];
    }*/

    if (s1.length() > s2.length()) maxLen = s1.length();
    else maxLen = s2.length();

    //cout << "\n";
    while (idx >= MAX - maxLen-1) {
        int sum = a[idx] + b[idx];

        int carry = sum / 10;

        if (carry > 0) {    // 올림수가 있다면
            a[idx - 1] += carry;
            sum %= 10;
        }
        res[idx] = sum;
        idx--;
        //cout << sum << endl;
    }
    //cout << "\n";

    while (res[idx] == 0)    idx++;

    for (int i = idx; i < MAX; i++) {
        
        cout << res[i];
    }
    return 0;
}
