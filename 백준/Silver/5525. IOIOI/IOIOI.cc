#include <iostream>

using namespace std;

int main() {
    // N+1개의 I와 N개의 O
    // n: 1 => I 2개와 O 1개인 IOI
    // n: 2 => I 3개와 O 2개인 IOIOI

    int n, len;
    cin >> n >> len;

    string str;
    cin >> str;

    // 찾아야 하는 문자열 만들기
    string find = "";
    int findLen = (n + 1) + n;

    while (findLen--) {
        if (findLen % 2 == 0)   // 짝수번째는 I
            find += "I";
        else
            find += "O";
    }

    int cnt = 0;
    findLen = (n + 1) + n;
    for (int i = 0; i <= len - findLen; i++) {
        string tmp = str.substr(i, findLen);    // i번째부터, findLen만큼 찾기

        if (tmp == find)
            cnt++;
    }
    cout << cnt << endl;
}