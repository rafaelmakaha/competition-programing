// https://atcoder.jp/contests/abc177/tasks/abc177_c
#include <bits/stdc++.h>

using namespace std;

int main(){
    unsigned long long n, sum=0, num;
    vector<int> v;

    cin >> n;

    while(cin >> num)
        v.push_back(num);

    unsigned long long i=0,j=1;
    while(i<j){
        j = i+1;
        while(j<n){
            sum += v[i]*v[j];
            j++;
        }
        i++;
    }
    cout << sum << endl;
    return 0;
}