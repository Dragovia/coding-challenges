
#include <iostream>

using namespace std;

int main()
{
   string message;
   int total = 0;

   cin >>message;

   for(int i = 0; i < message.length(); i++){
        if (i%3 == 0 && message[i] != 'P')
            total++;
        if (i%3 == 1 && message[i] != 'E')
            total++;
        if (i%3 == 2 && message[i] != 'R')
            total++;
   }

   cout << total;

    return 0;
}

