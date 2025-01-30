#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
using namespace std;

// 항공권이 중복이 되는 경우도 존재!

map <pair<string, string>, int> ticNum;    // 티켓별 사용 여부
map<string, vector<string>> m;  // 여행지별 위치

void dfs(string now, vector<string> &answer){
    
    //queue <string> q;
    //q.push(depart);
    
   // while(q.size())
    //{
        //string now = q.front();
        
        //q.pop();
       //answer.push_back(now);
        
        for(string e:m[now])
        {
            if(ticNum[{now, e}] != 0)
            {
                ticNum[{now, e}]--;
                dfs(e, answer);
                //q.push(e);
            }
        } 
    answer.push_back(now);
    //}
    
    
    
}

vector<string> solution(vector<vector<string>> tickets) {
    vector<string> answer;
    
    // 내부는 set로, 자동 정렬
    //map<string, int> cost; // 방문여부
    
    for (int i = 0; i< tickets.size(); i++)
    {
        m[tickets[i][0]].push_back(tickets[i][1]);
        ticNum[{tickets[i][0], tickets[i][1]}]++;
    }
    
    for(auto& [key, vec]:m)
    {
        sort(vec.begin(), vec.end());
    }
    
    dfs("ICN", answer);
    reverse(answer.begin(), answer.end()); // 경로 뒤집기
    return answer;
}