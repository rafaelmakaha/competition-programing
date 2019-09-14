#include<bits/stdc++.h>

using namespace std;

int main(){
    int n, v, total;
    float aux=0;
    
    cin >> v >> n;

    total = v * n;
    
    for(float i=0.1; i < 1; i += 0.1){
        aux = total * i;
        cout << "result: " << (aux - int(aux)) << endl;
        if(aux - (int(aux)) > 0.0){
            aux++;
        }

        if(i != 0.9) printf("%d ", int(aux));
        else  printf("%d\n", int(aux));
    }
    return 0;
}