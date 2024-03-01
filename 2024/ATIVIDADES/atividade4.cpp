#include <stdio.h>
#include <iostream>

using namespace std;

int main(){
    int salario;
    int vendas;

    cout << "Insira seu salario fixo" << endl;
    cin >> salario;
    cout << "Insira o valor das vendas" << endl;
    cin >> vendas;

    int bonus = vendas + (vendas * 0.03);
    cout << bonus;
    salario = salario + bonus;

    if (salario > 20000){
        cout << "Parabens, atingiu a meta, seu salario com bonus é de: " << salario + 600 << endl;
    }
    
    return 0;
}