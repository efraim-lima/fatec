#include <iostream>
#include <conio.h>

using namespace std;

int main(){
    int numero;
    cout << "Digite um numero: " << endl;
    cin >> numero;

    if (numero % 3 == 0 and numero % 5 == 0)
        cout << "O numero é divisível por 3 e por 5" << endl;
        else{
            cout <<  "O numero NÃO é divisível por 3 e por 5" << endl;
        };

    cout << "Digite qualquer tecla para sair;" << endl;
    getch();
    return 0;
};