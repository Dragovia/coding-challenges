#include <iostream>
#include <iomanip>
using namespace std;

int a;
int b;
int aprime;
int bprime;

int main()
{
    cin >> a;
    cin >>b;
    for(int i = 0; i < 3; i++){

  
    aprime = (a%10) + aprime *10;
    bprime = (b%10) + bprime * 10;
    a = a/10;
    b = b/10;
    }
 
    if( aprime > bprime)
        cout << aprime;
    else{
        cout << bprime;
    }
}
