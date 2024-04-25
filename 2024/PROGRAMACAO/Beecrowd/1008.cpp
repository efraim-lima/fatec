#include <stdio.h>
#include <iostream>
#include <iomanip>

using namespace std;

/* g++ -o hi hi.cpp*/ 

int main(){
  int number;
  float amount, worked_hours, salary;

  cin >> number;
  cin >> worked_hours;
  cin >> amount;

  salary = amount * worked_hours;

  cout << "NUMBER = " << number << endl;
  cout << "SALARY = U$ " << fixed << setprecision(2) << salary << endl;
  return 0;
}
