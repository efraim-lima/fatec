#include <iostream>

using namespace std;

int main(){
    float litros = 0;
    cout << "Insira a quantidade de litros" << endl;
    cin >> litros;

    char combustivel;
    cout << "Insira qual combustivel selecionado, A, G ou D." << endl;
    cin >> combustivel;

    float a = 3.9;
    float g = 4.9;
    float d = 5.9;

    if(combustivel == 'a'){
        cout << "O valor a ser pago é: " << litros * a << endl;

    } 
    else if(combustivel == 'g'){
        cout << "O valor a ser pago é: " << litros * g << endl;
    }
    else {
        cout << "O valor a ser pago é: " << litros * d << endl;
    }

    switch(combustivel) {
        case 'a': cout << "a" << endl; break;
        case 'g': cout << "g" << endl; break;

    }

    return 0;
}