#include<iostream>
#include <bits/stdc++.h>
#include<string>
#include<algorithm>

using namespace std;

int main(){
    string entrada;
    cin >> entrada;
    int a = count(entrada.begin(), entrada.end(), 'a');
    int total = entrada.size();


    while(a <= total/2){
        total--;
    }

    cout << total << '\n';

    return 0;
}