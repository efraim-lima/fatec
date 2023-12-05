#include <iostream>
#include <list>
#include <conio.h>
#include <algorithm>
#include <string>

using namespace std;

int main(){
    list<string> vogais = {"a", "e", "i", "o", "u"};
    list<string> numeros = {"1","2","3","4","5","6","7","8","9","0"};
    
    cout << "Digite uma letra ou numero: " << endl;
    
    string caracter;
    cin >> caracter;

    transform(caracter.begin(), caracter.end(),caracter.begin(), ::tolower);

    if (find(vogais.begin(), vogais.end(), caracter) != vogais.end()){
        cout << "O caractere digitado é uma vogal!" << endl;
        }
    else if (find(numeros.begin(), numeros.end(), caracter) != numeros.end()){
        cout << "O caracter digitado é um numero!" << endl;
    }
    else {
        cout << "Parece que digitou uma consoante. \n Certifiue-se do que digitou anteriormente, por favor \n";
    }

    cout << "\nDigite qualquer tecla para sair;" << endl;

    getch();

    return 0;
}