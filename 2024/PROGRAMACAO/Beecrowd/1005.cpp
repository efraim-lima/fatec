#include <stdio.h>
#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    double A,B;
    float Avarage;
    
    cin >> A;
    cin >> B;

    A += A * 3.5;
    B += B * 7.5;
    Avarage = (A + B)/11.0;
    
    cout << "MEDIA = " << fixed << setprecision(5) << Avarage << endl;

    return 0;
}

