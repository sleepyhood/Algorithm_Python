#include<iostream>
#include<vector>
#include<algorithm>
#define DIV 1'000'000'007
using namespace std;

typedef long long ll;

int n;
int c, a;
ll b;
ll arr[1'000'001];
ll seg[1'000'001 * 4];

ll init(int node, int s, int e)
{
    if (s == e) return seg[node] = arr[s];
    int mid = (s + e) / 2;
    return seg[node] = (init(2 * node, s, mid) * init(2 * node + 1, mid + 1, e)) % DIV;
}

ll query(int node, int s, int e, int l, int r) {
    if (e < l || r < s)
        return 1;
    if (l <= s && e <= r)
        return seg[node];
    int mid = (s + e) / 2;
    return (query(2 * node, s, mid, l, r) * query(2 * node + 1, mid + 1, e, l, r)) % DIV;
}


ll update(int node, int s, int e, int idx, ll val)
{
    if (s == e) return seg[node] = val; // start 와 end 의 위치가 일치하면 input[start] 값을 넣어준다.
    int mid = (s + e) / 2;
    if (idx <= mid) 
        update(2 * node, s, mid, idx, val);
    else 
        update(2 * node + 1, mid + 1, e, idx, val);
    ll t1 = seg[2 * node];
    ll t2 = seg[2 * node + 1];
    return seg[node] = (t1*t2) % DIV; // 다른 노드들의 정보를 
}

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int q1, q2;
    cin >> n >> q1 >> q2;
    for (int i = 1; i <= n; i++)
    {
        cin >> arr[i];
        arr[i] %= DIV;
    }

    init(1, 1, n); // 세그먼트 트리 만들기
    //for (int i = 1; i <= 4 * n; i++) {
    //    cout << seg[i] << " ";
    //}
    //cout << endl;
    q1 += q2;

    while (q1--) {
        cin >> c >> a >> b;

        if (c == 2)
            cout << query(1, 1, n, a, b) << "\n";

        else {
            arr[a] = b%DIV;
            update(1, 1, n, a, b);
        }
        //for (int i = 1; i <= 4*n; i++) {
        //    cout << seg[i] << " ";
        //}
        //cout << endl;

    }
}