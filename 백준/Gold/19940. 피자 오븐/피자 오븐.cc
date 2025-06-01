#include <stdio.h>

int main()
{
	int n = 0;
	scanf("%d", &n);
	while (n--)
	{
		int arr[5] = {};//+60,+10,-10,+1,-1;
		int btn[5] = { 60,10,-10,1,-1 };
		int t = 0;
		int k = 0;
		scanf("%d", &k);
		while (1)
		{
			//printf("도는중 %d %d\n", t, k);
			if (t == k)
				break;
			int t1 = 2100000000;
			int t2 = -1;
			for (int i = 0; i < 5; i++)
			{
				int tmp = t + btn[i];
				if (tmp < 0)tmp = 0;
				int tt = 0;
				if (tmp > k)tt = tmp - k;
				else tt = k - tmp;
				//printf("%d 일 때 차이 %d\n", i, tt);
				if (tt <= t1)
				{
					t1 = tt;
					t2 = i;
			//		printf("%d로 바꿈 %d\n", t2,tt);
				}
				
			}
		//	printf("%d를 더하는게 제일 좋습니다\n", t2);
			t += btn[t2];
			arr[t2]++;
		}
		for (int i = 0; i < 5; i++)
		{
			printf("%d ", arr[i]);
		}
		printf("\n");
		
	}
	return 0;
}