#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string.h>

std::vector<int>v[1000010];

std::vector<int>tree[1000010];

int dp[1000010][2] = {};
int visit[1000010] = {};

int f(int w, int al)
{

	if (dp[w][al] > -1)
		return dp[w][al];

	dp[w][al] = al;

	for (int i : tree[w])
	{
		if (al == 0)
			dp[w][al] += f(i, 1);
		else
			dp[w][al] += std::min(f(i, 1), f(i, 0));
	}

	return dp[w][al];
}

void make(int w)
{
	for (int i : v[w])
	{
		if (visit[i])
			continue;
		visit[i] = w;
		tree[w].push_back(i);
		make(i);
	}
}


int main()
{
	memset(dp, -1, sizeof(dp));
	int n = 0;
	scanf("%d", &n);
	int a = 0, b = 0;
	for (int i = 1; i < n; i++)
	{
		scanf("%d %d", &a, &b);
		v[a].push_back(b);
		v[b].push_back(a);
	}
	

	visit[1] = -1;
	make(1);

	printf("%d", std::min(f(1, 0), f(1, 1)));


	
	return 0;
}