#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> lista = {1,2,3,4,5,6,7,8,9,10};
    vector<int> lista_inversa = {};

    int i = 1;
    int tamanho = lista.size();

    while( i <= tamanho){
        lista_inversa.insert(lista_inversa.end(), lista[tamanho - i]);
        i++;
    };

    for (int elemento : lista_inversa){
        cout << elemento << endl;
    };

    return 0;
}