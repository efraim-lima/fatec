#include <iostream>

using namespace std;

int main(){
    int quantidade = 0;
    cout << "Insira a quantidade atual em estoque: ";
    cin >> quantidade;

    int maximo = 0;
    cout << "Insira o maximo atual: ";
    cin >> maximo;

    int minimo = 0;
    cout << "Insira o minimo atual: ";
    cin >> minimo;

    int media = 0;
    media = (maximo + minimo)/2;

    if (quantidade < media){
        cout << "Seu estoque esta abaixo da media, faça outra compra";
    }
    else {
        cout << "Seu estoque parece estar ok";
    };

    return 0;
}