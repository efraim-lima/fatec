#include <iostream>
#include <stdio.h>
#include <iomanip>

using namespace std;

int main(){
  int code, units, code2, units2;
  double price1, price2, total;

  cin >> code;
  cin >> units;
  cin >> price1;

  cin >> code2;
  cin >> units2;
  cin >> price2;

  total = (units * price1) + (units2 * price2);

  cout << fixed << setprecision(2) << total << endl;

  return 0;
}
