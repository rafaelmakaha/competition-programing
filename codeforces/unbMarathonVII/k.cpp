#include<bits/stdc++.h>

using namespace std;

int main(){
    int l, c;
    int x=-1, y=-1;
    string p;
    cin >> l >> c;

    for(int i=0; i < l; i++){
        cin >> p;
        for(int j = 0; j < c; j ++){
            if(p[j] == 'W'){
                x = i+1;
                y = j+1;
            }
        }
    }

    cout << x << " " << y << endl;

    return 0;
}