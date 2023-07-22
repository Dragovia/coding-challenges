#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
using namespace std;


int b,d,c,l; /// bdc are all legs  , l is total number of legs
//bdc is 0 to 100
//l is 0 to 250
vector<string> thing;
bool cursed = true;
bool never = false;
bool unlucky ( int xx,int yy){
  if(xx + yy == 13)
    return 1;

  else return 0;
}

int x,y;

  int maxx = 16;

int main() {

 cin >> x >> y;
while ( x != 0 && y !=0){
  maxx--;
  if(maxx == 0){
  break;
  }
  
if(x + y == 13){
  //cout << x + y;
 //cout <<"Never speak again.\n" ;
  thing.push_back("Never speak again.\n");
}
  


  
 else if ( x > y){
    if (unlucky(x,y) == 1)
    continue;
   
   //cout << "To the convention.\n";
   thing.push_back("To the convention.\n");
 }
  

  

  else if(x < y){
 if (unlucky(x,y) == 1)
    continue;
    
 //  cout << "Left beehind.\n";
      thing.push_back("Left beehind.\n");
  }

  else if ( x == y){
   // cout << "Undecided.\n";
    thing.push_back("Undecided.\n");
  }

 cin >> x >> y; 
}

  for(int i = 0; i <thing.size(); i++){
   if (thing[i] == "Never speak again.\n"){
    // cout <<"Never speak again.\n";
     never = true;
    break;
     
   }

  }

 

  if (never == true){
    
  for(int i = 0; i <thing.size(); i++){
   cout << thing[i];
   }

  }
  
 // }
  
  

  
}