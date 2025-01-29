#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int n, m; 
vector <int> v[32001];
int arr[32001];

int main() {
    cin >> n >> m;

    for (int i = 0; i < m; i++)
    {
        int a, b;
        cin >> a >> b;
        v[a].push_back(b);
        arr[b]++;   // b의 indegree
    }
        
    queue<int>q;
    vector<int> result;

    for (int i = 1; i <= n; i++)
    {
        if (arr[i] == 0)
        {
            q.push(i);
        }
    }

    while (q.size())
    {
        int now = q.front();
        result.push_back(now);  
        
        q.pop();
        
        for (int e : v[now])
        {
            arr[e]--;

            if (arr[e] == 0)
            {
                q.push(e);
            }
        }
    }

    for (int e : result)
    {
        cout << e << " ";
    }

}