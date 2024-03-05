#include <iostream>

using namespace std;

int main() {
    int soma, media, comprimento, nota1, nota2, nota3;

    cout << "Digite a primeira nota: " << endl;
    cin >> nota1;
    cout << "Digite a segunda nota: " << endl;
    cin >> nota2;
    cout << "Digite a terceira nota: " << endl;
    cin >> nota3;

    int lista[] = {nota1, nota2, nota3};

    soma = nota1 + nota2 + nota3;
    comprimento = sizeof(lista) / sizeof(lista[0]);

    cout << sizeof(lista) << endl;
    cout << sizeof(lista[0]) << endl;
    cout << comprimento << endl ;

    media = soma / comprimento;
    cout << "A média de notas deste aluno é: " << media << endl;

    if (media >= 7) {
        cout << "Aluno Aprovado!" << endl;
    } else {
        cout << "Aluno não foi aprovado" << endl;
    };

    return 0;
}