#include <stdio.h>
#include <iostream>
#include <iomanip>

using namespace std;

int main(){
  string name;
  float fixo, total, salary;

  cin >> name;
  cin >> fixo;
  cin >> total;

  salary = fixo + total * 0.15;

  cout << "TOTAL = R$ " << fixed << setprecision(2) << salary << endl;

  return 0;
}
