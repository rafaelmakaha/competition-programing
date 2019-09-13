#include<bits/stdc++.h>

using namespace std;

int main(){
    int n;
    string s, ans="";
    
    cin >> n;
    cin >> s;

    

    for (auto c: s){
        ans[ans.length()/2] = c;
        cout << c << endl;
    }

    cout << ans << endl;

    return 0;
}