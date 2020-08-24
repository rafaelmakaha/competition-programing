//https://codeforces.com/problemset/problem/617/A
#include <bits/stdc++.h>

using namespace std;

int main(){
    int x, sum=0;

    cin >> x;
    while(x > 0){
        if (x >= 5){
            sum += x/5;
            x = x%5;
        }else if (x >= 4){
            sum += x/4;
            x = x%4;
        }else if (x >= 3){
            sum += x/3;
            x = x%3;
        }else if (x >= 2){
            sum += x/2;
            x = x%2;
        }else if (x >= 1){
            sum += x/1;
            x = x%1;
        }
    }
    cout << sum << endl;
    return 0;
}