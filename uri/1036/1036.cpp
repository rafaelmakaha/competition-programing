#include<bits/stdc++.h>

using namespace std;

int main(){
	double a,b,c, delta, r1, r2;

	cin >> a >> b >> c;

	delta = pow(b,2) -4 * a * c;	

	if (delta < 0 || a == 0.0){
		cout << "Impossível calcular\n";
		return 0;
	}
	
	r1 = (-b + sqrt(delta)) / (2 * a);
	r2 = (-b - sqrt(delta)) / (2 * a);
	
	cout << "R1 = " << fixed << r1 << endl;
	cout << "R2 = " << fixed << r2 << endl;

	return 0;
}
