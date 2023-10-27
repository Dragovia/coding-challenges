#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

int main() {

string keyStr;
unsigned int i;
int smallest = 0;
int data [5] = {2,4,1,16,0};
int getArrayLength = sizeof(data)/sizeof(int);


/*for(int i = 0; i < getArrayLength; i++)
{
    if(data[i]> data[i + 1])
        data[i + 1] = data[i];

    cout << data[i]<<endl;
}
*/
getline(cin, keyStr);

for( i = 0; i< keyStr.size(); i++){
 if(int(char(keyStr[i])) < 65)
    keyStr[i] = 'y';

 if( int(char(keyStr[i]))> 122)
    keyStr[i] = 'y';

    //cout <<keyStr[i];
}
cout << "Valid password: " << keyStr <<endl; 



return 0;
}

