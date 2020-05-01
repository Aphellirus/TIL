#include <iostream>
using namespace std;
int main()
{
  int a, b, c, i, n;
  cout << " Enter the number of digits you want " << endl;
  cin >> n;
  cout << endl;
  a = 0;
  b = 1;
  for (i = 1; i <= n; i++)
  {
    c = a + b;
    a = b;
    b = c;
    c = a + b;
    cout << a << endl;
  }
  cout << "Golden Ratio" << endl
     << (double)b / a;
  return 0;
}
