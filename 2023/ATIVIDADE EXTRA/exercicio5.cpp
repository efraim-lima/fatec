#include <iostream>
#include <numeric>
#include <vector>
#include <conio.h>

using namespace std;

int main(){
    vector<float> lista = {1,2,3,4,5,6,7,8,9,9.3, 9.2, 10};
    vector<float> maiores_que_6 = {};

    float maior = lista[0], menor = lista[0], soma = 0.0;
    
    for (float i : lista){
        if (i > maior){
            maior = i;
        }
        if (i < menor){
            menor = i;
        }
        if (i > 6){
            maiores_que_6.insert(maiores_que_6.end(), i);
        }

    }
    soma = accumulate(lista.begin(), lista.end(), 0);
    float media = soma / lista.size();

    cout << "A maior nota é: " << maior << endl;
    cout << "A menor nota é: " << menor << endl;
    cout << "A lista de notas maiores que 6 é: ";
    for (float item : maiores_que_6) {
        std::cout << item << " ";
    }
    cout << "A soma das notas é: " << soma << endl;
    cout << "A quantidade de notas na lista é: " << lista.size() << endl;
    cout << "A média das notas é: " << media << endl;
    
    cout << "Digite qualquer tecla para sair. ";
    getch();

    return 0;
}