#include <bits/stdc++.h>

using namespace std;

int main(){
    string st,aux;
    int i=0,p=0,a=1;
    vector<string> ans;
    cin >> st;

    while(i <= st.length()){
        if(st[i] == 'x'){
            p = i;
            while (st[p] == 'x'){
                p++;
            }
            aux = "Comando " + a ;
            aux += ": (x)" + p-i;
            ans.push_back(aux);
            a++;
            i = p;
        }else if(st[i] == 'o'){
            p = i;
            while(st.substr(p,p+1) == "ox"){
                p += 2;
            }
            aux = "Comando " + a ;
            aux += ": (ox)" + (p-i)/2;
            ans.push_back(aux);
            a++;
            i = p;
        }else{
            p = i;
            while(st[p] != '.'){
                p++;
            }
            aux = "Comando " + a ;
            aux += ": (.)" + st.substr(i+1,p-1);
            aux += "]";
            ans.push_back(aux);
            a++;
            i = p + 1;
        }
    }
    for(auto c: ans){
        cout << c << endl;
    }


    return 0;
}