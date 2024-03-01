#include <iostream>
#include <conio.h>

using namespace std;

int main(){
    int maior, numero1, numero2, numero3;

    cout << "Digite o primeiro numero" << endl;
    cin >> numero1;
    cout << "Digite o segundo numero" << endl;
    cin >> numero2;
    cout << "Digite o terceiro numero" << endl;
    cin >> numero3;

    if (numero1 > numero2 && numero1 > numero3) {
        maior = numero1;}
    else if (numero2 > numero1 && numero2 > numero3) {
        maior = numero2;}
    else {
        maior = numero3;
    }

    cout << "O maior numero é: " << maior << endl;
    cout << "Digite qualquer tecla para sair";
    getch();
}