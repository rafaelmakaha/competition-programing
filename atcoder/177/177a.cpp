// https://atcoder.jp/contests/abc177/tasks/abc177_a
#include<bits/stdc++.h>

using namespace std;

int main(){
    int d,t,s;
    cin >> d >> t >> s;
    if(!s){
        cout << "No" << endl;
        return 0;
    }

    if(d/s <= t)
        cout << "Yes" << endl;
    else
        cout << "No" << endl;
    return 0;
}