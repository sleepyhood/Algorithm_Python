#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
typedef struct _Mold
{
	int y;	// 행
	int x;	// 열
	int t;	// 전염 시간
}Mold;


int arr[100][100];
int visited[100][100];
int mr[] = { -1, 1, 0, 0, -1, -1, 1, 1 };
int mc[] = { 0, 0, -1, 1, 1, -1, -1, 1 };
//int tmp;
int cnt;
int n, m;
int days;

queue<Mold> q[100][100];		// 곰팡이 군집별 큐
// 날짜, 군집 번호 순서


/* 반례
5 3
100
000
000
000
003

110
333
333
333
333

과 같이, 빠른쪽이 뒤덮어야함.

*/
void dfs(int r, int c, int type, bool useQueue, int visited[][100])
{

	if (useQueue)
	{
		q[days][cnt].push({ r,c,type });

	}
	//cout <<r << " " << c << " " << type << "\n";

	visited[r][c] = type;

	for (int k = 0; k < 8; k++)
	{
		int nr = r + mr[k];
		int nc = c + mc[k];
		if (nr < 0 || nc < 0 || nr >= n || nc >= m)
			continue;
		if (visited[nr][nc])
			continue;
		if (arr[nr][nc] == 0)
			continue;
		if (arr[nr][nc] == type || (!useQueue))
		{
			dfs(nr, nc, type, useQueue, visited);
		}
	}

}

int main()
{
	cin >> n >> m;

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			scanf("%1d", &arr[i][j]);
		}
	}

	// 곰팡이가 있는 위치 기억해두기
	// 군집별로 배열에 저장
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (arr[i][j] && !visited[i][j])
			{
				//tmp = 0;
				dfs(i, j, arr[i][j], true, visited);	// 곰팡이가 있는 위치를 기억하므로, 큐도 사용해야함
				//cout << tmp << endl;
				//cout << q.size() << endl;

				cnt++;
			}

		}
	}

	int totalCnt = cnt;

	/*제일 짜증나는 부분*/

	// 곰팡이의 개수: cnt
	while (totalCnt > 1)	// 군집이 1개로 합쳐질 때까지
	{
		//dqys = 0;

		// 1. 군집의 개수 확인하기
		// 하나의 군집이 있는지만 확인하므로, 별도의 방문 배열이 필요
		int tmpvisit[100][100] = {};
		int sizeCheck = 0;
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				if (arr[i][j] && !tmpvisit[i][j])
				{
					dfs(i, j, arr[i][j], false, tmpvisit);

					sizeCheck++;
				}

			}
		}
		
		//printf("sizeCheck: %d\n", sizeCheck);
		if (sizeCheck == 1)
		{
			break;
		}
		totalCnt = sizeCheck;

		// 2. 각 군집(배열 인덱스로 구분)마다 전이
		for (int mol = 0; mol < cnt; mol++)	// 각 군집마다
		{
			int p = 0;
			if (q[days][mol].size())
				p = q[days][mol].front().t;
			//cout << p << endl;
			int current = 0;
			queue <Mold> tmp[100];

			// 각 군집의 속도에 따라 가는 양이 달라짐

			/*
				군집은 2k+1 격자로 퍼져감
				즉, 방향벡터에 배치해도 퍼지는 범위도 반복되어야 함.
				이를 반영하기 위해, 다음날이 아닌 임시 배열에 넣어두고 시뮬레이션 하긴
			*/
			// 2-1. 해당 군집을 임시 큐에 옮기기
			while (q[days][mol].size())
			{
				//printf("days: %d\tmol: %d\n", days, mol);
				int r = q[days][mol].front().y;
				int c = q[days][mol].front().x;
				int t = q[days][mol].front().t;

				tmp[0].push({ r,c,t });
				q[days][mol].pop();
			}

			// 임시큐를 쓰는 이유: 속도에 따라, 곰팡이가 커지는 크기가 다르므로
			// 2-2. 임시큐에서 속도만큼 반복하기 (예. 2라면, 군집이 0->1, 1->2 번 커짐)
			while (current < p)
			{
				while (tmp[current].size())
				{
					int r = tmp[current].front().y;
					int c = tmp[current].front().x;
					int t = tmp[current].front().t;

					tmp[current].pop();

					for (int k = 0; k < 8; k++)
					{
						int nr = r + mr[k];
						int nc = c + mc[k];
						if (nr < 0 || nc < 0 || nr >= n || nc >= m)
							continue;

						// 방문된 다음 지역이 더 큰 경우
						// 이미 방문이 되어있으면서, 다음지역의 속도가 더 빠른 경우
						if ( visited[r][c] <= visited[nr][nc])
							continue;

						// 자라는 속도가 빠른 곰팡이가 그 칸을 차지한다.
						// 즉, 방문된곳이여도 값을 비교해야함
						if (visited[r][c] > visited[nr][nc] || !visited[nr][nc])
						{
							tmp[current + 1].push({ nr,nc,t });
							visited[nr][nc] = t;
							//cout << "h" << endl;
						}

					}
				}
				current++;

			}
			//printf("tmp[current]: %d\n", tmp[current].size());

			// 2-3. 임시큐를 날짜별 큐에 옮기기
			while (tmp[current].size())
			{
				int r = tmp[current].front().y;
				int c = tmp[current].front().x;
				int t = tmp[current].front().t;

				q[days + 1][mol].push({ r,c,t });
				tmp[current].pop();
			}
			//printf("q[days + 1][mol].size(): %d\n", q[days + 1][mol].size());


		}
		
		//cout << "\n";

		// 3. 방문 여부를 원본 배열에 반영하기
		// 날짜마다 업데이트되어야함.
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				arr[i][j] = visited[i][j];
				//cout << visited[i][j] << " ";

			}
			//cout << endl;
		}

		days++;
	}

	cout << days << "\n";

	return 0;
}