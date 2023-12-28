#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    for(int i = 2; i < n ; i++){
        if(n%i == 1){
            answer = i;
            // 최소값이므로 구하면 바로 루프탈출
            break;
        }
    }
    return answer;
}