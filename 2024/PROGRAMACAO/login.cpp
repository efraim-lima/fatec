#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

int main(){
  string login = "";
  string senha = "";

  while(login != "ABC" && senha != "abc123"){
    cout << "Digite seu login: ";
    cin >> login;
    cout << "Digite sua senha: ";
    cin >> senha;

    if(login != "ABC" || senha != "abc123"){
      cout << "Acesso negado!" << endl;
    } else {
      cout << "Acesso concedido!" << endl;
    }
  };

  return 0;
}
