#include<bits/stdc++.h>

using namespace std;

int main(){
    map<string,int> dic;
    int n,m;
    string st;

    cin >> n ;

    cin >> st;

    for(int i=0; i < n-1; i++){
        cin >> m;
        if(st.find('8')==0){
            cout << "NO";
        }else if (st.length() == 11 && st[0] != 8){
            cout << "NO";
        }else 

        
    }


    return 0;
}