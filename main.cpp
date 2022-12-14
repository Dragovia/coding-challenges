#include <iostream>


using namespace std;

int main()
{
  int n,nprime;
  int numbers;
  int adding =0;
  bool flag = true;
  cin >> n;
  nprime = n;

  while(n != 0){
    numbers = n % 10;
    n = n/10;
    adding = adding + numbers;

       if(n == 0){
        if(nprime % adding !=0){
        adding = 0;
        numbers =0;
        n = nprime + 1;
        nprime = n;

        }
        else
        {
            cout << nprime;
        }
       }
  }

    return 0;
}
