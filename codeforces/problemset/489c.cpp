//https://codeforces.com/problemset/problem/489/C
#include <bits/stdc++.h>

using namespace std;

bool can(int m, int s){
    return s >= 0 && s <= 9 * m;
}

int main(){
    int m,s;
    cin >> m >> s;

    if (!s){
        cout << "-1 -1" << endl;
        return 0;
    }
    //minimum number
    int sum = s;
    char minn;
    for(int i=0; i < m; i++){
        for(int d=0; d < 10; d++){
            if((i > 0 || d > 0 || (m == 1 && d == 0 )) && can(m - i - 1, sum - d) ){
                minn += char('0' + d);
                sum -= d;
                break;
            }
        }
    }
    cout << minn << endl;

    return 0;
}