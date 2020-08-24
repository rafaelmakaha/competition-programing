// https://codeforces.com/problemset/problem/116/A
#include <bits/stdc++.h>

using namespace std;

int main(){
    int  n,a,b;
    int sum=0, max=0;

    cin >> n;

    for(int i=0;i<n;i++){
        cin >> a >> b;
        if(sum-a+b > max)
            max = sum-a+b;
        sum += -a+b;
    }
    cout << max << endl;
    return 0;
}