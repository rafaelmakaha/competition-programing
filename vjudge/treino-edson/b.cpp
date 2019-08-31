#include<bits/stdc++.h>

using namespace std;

int main(){
    int d,n;

    cin >> d >> n;

    if(d == 0){
        cout << n << endl;
    }else if(d == 1){
        if(n == 100) n++;
        cout <<  n * (100) << endl;
    }else if(d == 2){
        if(n == 100) n++;
        cout << n * (10000) << endl;
    }

    return 0;
}