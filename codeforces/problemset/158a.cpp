// https://codeforces.com/problemset/problem/158/A

#include <bits/stdc++.h>

using namespace std;

int main(){
    int n,k;
    vector<int> v;

    cin >> n >> k;

    int num;
    while(cin >> num)
        v.push_back(num);

    int ans=0;
    for(int i=0; i < int(v.size()); i++){
        if(v[i] >= v[k-1] && v[i] > 0)
            ans++;
    }


    cout << ans << endl;
    
    return 0;
}