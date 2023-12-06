#include <iostream>
#include <cctype> // Para toupper
#include <string>
#include <conio.h>

using namespace std;

int main(){
    float temperatura, temperatura2;
    char metrificacao;

    cout << "Digite 'C'  para converter de Celsius para Fahrenheit ou 'F' para converter de Fahrenheit para Celsius: " << endl;
    cin >> metrificacao;
    metrificacao = toupper(metrificacao);
    cout << "Digite a temperatura: " << endl;
    cin >> temperatura;

    if (string(1, metrificacao)=="C") {
        temperatura2 = (temperatura * 1.8) + 32;
        cout << temperatura << " é equivalente a "<< temperatura2 << endl;
    } else if (string(1, metrificacao)=="F") {
        temperatura2 = ((temperatura - 32) / 1.8);
        cout << temperatura << " é equivalente a "<< temperatura2 << endl;
    } else {
        cout << "Não entendi algo, por favor, volte ao começo" << endl;
    }

    cout << "Digite qualquer tecla para sair. ";
    getch();
    return 0;
}