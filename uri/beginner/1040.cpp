#include <bits/stdc++.h>
#include <stdio.h>
#include <iomanip>

using namespace::std;

int main() {
    double n1, n2, n3, n4, media;

    cin >> n1 >> n2 >> n3 >> n4;

    media = (n1 * 2 + n2 * 3 + n3 * 4 + n4)/10;
    cout << "Media: " << fixed << setprecision(1) << media << endl;

    if (media < 5.0) {
        cout << "Aluno reprovado." << endl;
    } else if (media > 6.9) {
        cout << "Aluno aprovado." << endl;
    } else {
        cout << "Aluno em exame." << endl;
        cin >> n1;
        cout << "Nota do exame: " << fixed << setprecision(1) << n1 << endl;
        media = (media + n1)/2;
        if (media > 5.0) {
            cout << "Aluno aprovado." << endl;
        } else {
            cout << "Aluno reprovado." << endl;
        }
        cout << "Media final: " << fixed << setprecision(1) << media << endl;
    }

    return 0;
}