#include<bits/stdc++.h>

using namespace std;

int main(){
	float a,b,c, delta, r1, r2;

	cin >> a >> b >> c;

	delta = b*b-4*a*c;	

	if (delta < 0 || a == 0){
		cout << "Impossível calcular\n";
		return 0;
	}
	
	r1 = (-b + sqrt(delta)) / (2 * a);
	r2 = (-b - sqrt(delta)) / (2 * a);
	printf("R1 = %.5f\nR2 = %.5f\n", r1, r2);

	return 0;
}
