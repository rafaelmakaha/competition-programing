// https://codeforces.com/problemset/problem/791/A
#include<bits/stdc++.h>

using namespace std;

int main() {
    int a,b,t=0;

    cin >> a >> b;

    while(b >= a){
        t++;
        b*=2;
        a*=3;
    }
    cout << t << endl;
    
    return 0;
}