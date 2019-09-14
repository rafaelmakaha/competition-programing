#include<bits/stdc++.h>

using namespace std;

int main(){
    int n, c, aux;

    cin >> n;
    cin >> c;

    bool flag = false;

    for(int i=0; i < n-1 ; i++){
        cin >> aux;
        if (aux > c){
            flag = true;
        }
    }
    if(flag){
        cout << "N" << endl;
        return 0;
    }
    cout << "S" << endl;

    return 0;
}