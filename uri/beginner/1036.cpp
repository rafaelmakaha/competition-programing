#include<bits/stdc++.h>
#include<iomanip>

using namespace std;

int main(){
	float a,b,c, delta, r1, r2;

	cin >> a >> b >> c;

	delta = b*b-4*a*c;	

	if (delta < 0 || a == 0){
		cout << "Impossivel calcular" << endl;
	} else {
		r1 = (-b + sqrt(delta)) / (2 * a);
		r2 = (-b - sqrt(delta)) / (2 * a);
		cout << "R1 = " << fixed << setprecision(5) << r1 << endl;
		cout << "R2 = " << fixed << setprecision(5) << r2 << endl;
	}
	

	return 0;
}
