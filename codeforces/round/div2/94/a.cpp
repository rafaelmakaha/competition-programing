// https://codeforces.com/contest/1400/problem/A
#include <bits/stdc++.h>

using namespace std;

int main(){
    int casos,n;
    string s;
    string aux, aux2, aux3;
    
    cin >> casos;

    while(casos){
        cin >> n;
        cin >> s;
        aux = s.substr(0,n);
        aux3 = aux;
        if(n > 1){
            for(int i=1; i < 2*n-1; i++){
                aux2 = s.substr(i, n+i);
                for(int j=0; j < n+i; j++){
                    if(aux[j] == aux2[j])
                        aux3[j] = aux[j];
                }
                aux = aux3;
            }
        }
        cout << aux << endl;
        casos--;
    }
    return 0;
}