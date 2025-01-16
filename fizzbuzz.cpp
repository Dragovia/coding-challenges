#include <iostream>
using namespace std;

int main()
{
    int x,y,sizee;
    cin >> x >> y >> sizee;
    
    
    for(int i = 1; i <= sizee; i++){
        
       if((i % y ==0) && (i % x ==0) ){
            cout << "FizzBuzz"<<endl;
        }
        
        
        if((i % x ==0) && (i % y !=0) ){
            cout << "Fizz"<<endl;
        }
        
         if((i % y ==0) && (i % x !=0) ){
            cout << "Buzz"<<endl;
        }

        
        
          if((i % y !=0) && (i % x !=0) && i >= 1){
            cout << i<<endl;
        }
        
        
        
        
    }

    return 0;
} 