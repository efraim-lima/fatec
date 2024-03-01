#include <iostream>
#include <string>
#include <conio.h>

using namespace std;

int main() {
    string senha = "123", senha_input;
    int tentativas = 0, erros = 0, limite = 3;

    while(tentativas < limite){
        cout << "\nDigite a Senha: ";
        cin >> senha_input;

        if (senha_input != senha) {
            cout << "Senha incorreta." << endl;
           
            tentativas++;
           
            if (tentativas < limite){
                cout << "Você ainda possui " << limite - tentativas << " tentativas. " << endl;
            }
           
            erros++;
            continue;
        } else {
            cout << "Senha correta, login efetivado. " << endl;
            tentativas++;
            break;
        };
    };
    if (erros == 3) {
        cout << "Voce esgotou suas tentativas. Acesso negado. " << endl;
    };

    cout << "Você tentou " << tentativas << " vezes. " << endl << "Você errou " << erros << " vezes." << endl;
    cout << "Digite qualquer tecla para sair. ";
    getch();


    return 0;
}