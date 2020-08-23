#include <bits/stdc++.h>

using namespace std;

int main(){
    int n,k;
    vector<int> v(50);

    cin >> n >> k;

    int i=0;
    while(cin >> v[i])
        i++;

    for(int i: v){
        cout << i << " ";
    }
    cout << "olouco!";
    return 0;
}