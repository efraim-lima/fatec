#include <iostream>
#include <vector>
#include <conio.h>

using namespace std;

int main(){
    vector<int> lista = {1,2,3,4,5};

    for (int i : lista){
        cout << i << endl;
    };

    cout << "Digite qualquer tecla para sair. ";
    getch();

    return 0;
}