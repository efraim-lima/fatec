#include <stdio.h>
#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    double A,B,C;
    float Avarage;
    
    cin >> A;
    cin >> B;
    cin >> C;

    Avarage = (2 * A + 3 * B + 5 * C)/10.0;
    
    cout << "MEDIA = " << fixed << setprecision(1) << Avarage << endl;

    return 0;
}