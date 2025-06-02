#include <iostream>
#include <queue>
#include <vector>
#include <string>
using namespace std;

struct State {
    int y, x, broken, dist, is_day;
};

int n, m, k;
int dy[4] = {-1, 1, 0, 0};
int dx[4] = {0, 0, -1, 1};
vector<string> miro;
bool visited[1000][1000][11][2]; // y, x, 벽 부순 횟수, 낮밤

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m >> k;
    miro.resize(n);
    for (int i = 0; i < n; ++i) {
        cin >> miro[i];
    }

    queue<State> q;
    q.push({0, 0, 0, 1, 1}); // 시작 위치, 벽 안부숨, 거리 1, 낮
    visited[0][0][0][1] = true;

    while (!q.empty()) {
        State cur = q.front(); q.pop();
        int y = cur.y, x = cur.x, broken = cur.broken, dist = cur.dist, is_day = cur.is_day;

        if (y == n - 1 && x == m - 1) {
            cout << dist << "\n";
            return 0;
        }

        for (int d = 0; d < 4; ++d) {
            int ny = y + dy[d];
            int nx = x + dx[d];

            if (ny < 0 || ny >= n || nx < 0 || nx >= m) continue;

            if (miro[ny][nx] == '0' && !visited[ny][nx][broken][is_day ^ 1]) {
                visited[ny][nx][broken][is_day ^ 1] = true;
                q.push({ny, nx, broken, dist + 1, is_day ^ 1});
            }

            else if (miro[ny][nx] == '1' && is_day == 1 && broken < k && !visited[ny][nx][broken + 1][is_day ^ 1]) {
                visited[ny][nx][broken + 1][is_day ^ 1] = true;
                q.push({ny, nx, broken + 1, dist + 1, is_day ^ 1});
            }
        }

        // 밤이고 벽이 있어 진행 못 했을 때 -> 제자리 대기
        if (!visited[y][x][broken][is_day ^ 1]) {
            visited[y][x][broken][is_day ^ 1] = true;
            q.push({y, x, broken, dist + 1, is_day ^ 1});
        }
    }

    cout << "-1\n";
    return 0;
}
