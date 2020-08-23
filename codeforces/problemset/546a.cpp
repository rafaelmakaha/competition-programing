// https://codeforces.com/problemset/problem/546/A
#include <bits/stdc++.h>

using namespace std;

int main(){
    int k,n,w,ans;
    int sum=0;

    cin >> k >> n >> w;
    
    for(int i=1; i <= w; i++){
        sum+=i*k;
    }
    if (n >= sum)
        ans = 0;
    else
        ans = sum-n;
    cout << ans << endl;
    return 0;
}