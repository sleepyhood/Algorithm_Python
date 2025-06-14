#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include <iomanip>
#include <stack>
#include <queue>
using namespace std;



int main()
{
    int n, m = 0, cnt = 0, x, y;
    int l[] = { 0, 0, 1,-1 };
    int r[] = { 1,-1, 0, 0  };

    /*int l[] = { 0, 0, 1,-1 , 1,-1,1,-1 };
    int r[] = { 1,-1, 0, 0 , 1,-1,-1,1 };*/

    int arr[101][101] = { 0, };

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> x >> y;
        for (int u = y; u < y + 10; u++)
        {

            for (int j = x; j < x + 10; j++)
            {
                arr[u][j] = 1;
            }
            //144 30 16
        }
    }

    for (int i = 0; i < 101; i++)
    {
        for (int j = 0; j < 101; j++)
        {

          
                //if (i + 1 < 101 && i - 1 >= 0 && j + 1 < 101 && j - 1 >= 0)
                //{
                //    int down = arr[i][j] == 1 && arr[i + 1][j] == 0;
                //    int up = arr[i][j] == 1 && arr[i - 1][j] == 0;
                //    int right = arr[i][j] == 1 && arr[i][j + 1] == 0;
                //    int left = arr[i][j] == 1 && arr[i][j - 1] == 0;

                //    if (down) cnt++;
                //    if (up) cnt++;
                //    if (right) cnt++;
                //    if (left) cnt++;
                //    //if ( down || up || right || left) {
                //    //	vv[i][j] = 2;
                //    //	//count++;
                //    //}
                //}
                //cout << vv[i][j];
        

            if (arr[i][j] == 1) {
                if (i + 1 < 101 && i - 1 >= 0 && j + 1 < 101 && j - 1 >= 0)
                {
                    for (int k = 0; k < 4; k++) {
                        if (arr[i + l[k]][j + r[k]] == 0) {

                            cnt++;
                        }
                    }
                }
            }
            
            //cout << vv[i][j];
        }
        //cout << endl;
    }


    //for (int i = 0; i <= 100; i++)
    //{
    //    for (int j = 0; j <= 100; j++)
    //    {
    //        //m = 0;
    //        int tmp = 0;
    //        if (arr[i][j] == 2)
    //        {
    //            for (int k = 0; k < 4; k++)
    //            {
    //                if (i + l[k] >= 0 && i + l[k] < 100 && j + r[k] >= 0 && j + r[k] < 100)
    //                {
    //                    if (arr[i + l[k]][j + r[k]] == 0)
    //                    {
    //                        tmp++;
    //                    }
    //                }
    //            }
    //            if (tmp == 2)
    //                cnt++;
    //        }
    //       
    //        //if (m == 1)


    //        //cout << arr[i][j] << " ";
    //    }
    //    //cout << "\n";
    //}






    cout << cnt;
    return 0;
}