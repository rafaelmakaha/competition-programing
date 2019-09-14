#include<bits/stdc++.h>

using namespace std;

int main(){
    int n,c,t;
    string st;
    vector<int> v;

    cin >> n >> c >> t;
    cin >> st;

    for(auto c:st){
        if (c == ' ') continue;
        v.push_back(int(c));
    }
    int time = 0;
    bool flag;
    
    while(!v.empty() && time < 51){
        flag = true;
    
        time++;
    }


    return 0;
}