#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <stack>
#include <vector>
/*

5 5
1 1 1 1 1
2 3 4 5 6

*/
using namespace std;



vector<char> v;
int n, c;

bool check() {
	stack<char> st;
	stack<char> trash;

	for (int i = 0; i < v.size(); i++) {
		if (v[i] == '(') {
			st.push('(');
		}
		else if (st.size()) {
			st.pop();
		}
		else {
			trash.push(v[i]);
		}
	}
	if (st.size() || trash.size()) {
		return false;
	}
	return true;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> n;
	
	string s;
	cin >> s;

	int cursor = 0;


	for (int i = 0; i < s.length(); i++) {
		if (s[i] == '(') {
			v.insert(v.begin() + cursor, '(');
			cursor++;
		}
		if (s[i] == ')') {
			v.insert(v.begin()+cursor, ')');
			cursor++;
		}
		if (s[i] == '<' && cursor > 0) {
			cursor--;
		}
		if (s[i] == '>' && cursor < v.size()) {
			cursor++;
		}
		if (s[i] == 'X' && cursor != 0) {
			v.erase(v.begin() + cursor - 1);
			cursor--;
		}
		//cout << i + 1 << "번째: "<<cursor<<endl;
		/*for (char e : v) {
			cout << e;
		}*/
		//cout << "\n";
		if (check()) {
			//printf("%d번째는 실행됌\n",i + 1);
			//cout << s[i] << endl;
			//cout << "와" << (i + 1) << "\n\n";
			c = c ^ (i + 1);
		}

		//cout << "\n";
		//cout << c << "\n\n";
	}
	cout << c << "\n";

}