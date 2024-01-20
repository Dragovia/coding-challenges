#include <iostream>
#include <stack>

using namespace std;

int main()
{
    stack<int> staq;

    staq.push(21);
    staq.push(22);
    staq.push(24);
    staq.push(25);

    int num = 0;
    staq.push(num);

    while(!staq.empty()){
        cout << staq.top() << " ";
        staq.pop();
    }

    //staq.pop();
    //staq.pop();
cout << endl;
   while(!staq.empty()){
         cout << staq.top() << " ";
            //staq.pop();
         }

   if(staq.empty() )
    cout << "cheese";



    return 0;
}
