#include <string>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

const int maxHour = 1001;

bool compare(vector<int> a, vector<int> b){
    if(a[1] == b [1])
        return a[0] < b[0];
    else
        return a[1] < b [1];
}

int solution(vector<vector<int>> jobs) {
    int answer = 0;
    int start = 0;
    int spend = 0;
    
    vector<vector<int>> v;
    for(int i = 0 ; i< jobs.size(); i++){
        v.push_back(jobs[i]);
    }
    sort(v.begin(),v.end(), compare);
    // 소요시간 기준으로 정렬, 중복시 작업시점 비교
    
    while(!v.empty()){
        for(int i = 0 ; i < v.size() ; i++){
            // 요청시점은 
            if(v[i][0] <= start){
                spend += start + v[i][1] - v[i][0];
                start += v[i][1];
                v.erase(v.begin() +i);
                break;
            }
            if(i==v.size() - 1)
                start++;
        }
        
        
    }
    answer = spend / jobs.size();
    return answer;
}