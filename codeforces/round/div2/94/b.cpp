// https://codeforces.com/contest/1400/problem/B
#include <bits/stdc++.h>

using namespace std;

int can_take(int s, int w, int cs, int cw, int p){
    if(s > w)                                   // Verifica se sword é mais pesado do que axe
        return can_take(w, s, cw, cs, p);       // Chama a função para o mais leve
    if(s * cs >= p)                             // Verifica se a quantidade total do mais leve é menor do que o inventário
        return p / s;                           // Retorna a quantidade do item que pode ser carregada
    return 
}

int main(){
    int t, p,f,ns,nw,s,w;
    int total=0;
    int ans;
    
    cin >> t;
    while(t){
        cin >> p >> f;
        cin >> ns >> nw;
        cin >> s >> w;
        


        t--;
    }
    return 0;
}