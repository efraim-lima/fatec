#include <iostream>
#include <cstdio>
#include <conio.h>

using namespace std;

int main(){
    int ano;

    cout << "Digite um ano: ";
    cin >> ano;
    
    if (ano % 4 && (ano % 100 != 0 || ano % 400 == 0))
        cout << "O ano de " << ano << " é um ano bissexto. " << endl;
        else {
            cout << "O ano de " << ano << " não é um ano bissexto." << endl;
        }

    cout << "Digite qualquer tecla para sair" << endl;
    getch();
    return 0;
}