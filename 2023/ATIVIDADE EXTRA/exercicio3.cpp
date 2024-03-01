#include <iostream>
#include <vector>
#include <numeric>
#include <conio.h>

using namespace std;

int main(){
    vector<int> lista = {1,2,3,4,5};

    int soma;
   
    for (int i : lista){
        soma = accumulate(lista.begin(), lista.end(), 0);
    };

    cout << soma << endl;

    cout << "Digite qualquer tecla para sair. ";
    getch();

    return 0;
}