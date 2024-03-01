#include <iostream>
#include <conio.h>

using namespace std;

int main(){
    int comprimento1, comprimento2, comprimento3;

    cout << "Digite o primeiro comprimento" << endl;
    cin >> comprimento1;
    cout << "Digite o segundo comprimento" << endl;
    cin >> comprimento2;
    cout << "Digite o terceiro comprimento" << endl;
    cin >> comprimento3;

    if (comprimento1 == comprimento2 && comprimento1 == comprimento3){
        cout << "O triângulo é equilátero." << endl;
    } if (comprimento1 == comprimento2 || comprimento1 == comprimento3 || comprimento2 == comprimento3) {
        cout << "O triângulo é isóceles." << endl;
    } else {
        cout << "O triângulo é escaleno." << endl;
    };

    cout << "Digite qualquer tecla para sair. ";
    getch();
    return 0;
}