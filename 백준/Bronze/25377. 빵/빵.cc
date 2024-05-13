#include <iostream>
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    int n;
    cin>>n;
    int ans = 0;
    
    while(n--){
        int a, b;
        cin >> a>>b;
        if(a<=b){    // 도착이 가능하다면
            ans+=b-a;
        }
    }
    if(ans){ // 빵을 한번이라도 샀다면
        cout<<ans<<"\n";
    }
    else
        cout<<-1<<"\n";
    
    return 0;
}