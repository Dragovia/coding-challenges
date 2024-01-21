#include <iostream>
#include <iomanip>

using namespace std;

bool winner(int x, int y){
   if( x  == 1 && y == 2)
     return true;
    if( x  == 2 && y == 1)
     return true;
      
  else return false;
}

int pointDouble(int x, int y){
  if(x == y)
    return x + y;
}


int cases(int x,int y,int q,int r){
  if((x != y))

}


 int s0,s1,t0,t1;
 bool game = true;

int point2 = 0;
int point1 =0;
int point0 =0;
int player1= 0;
int player2 = 0;

int main() {

  while(game){

    cin >> s0 >> s1 >> t0 >> t1;
    if(s0 == 0 && s1== 0 && t0== 0 && t1 == 0 ){
      game = false;
    }

  if((s0+s1)==(t0+t1)){
          cout << "Tie.";
          point0 = point0 + 0;
        }

    cout << cases(s0,s1,t0,t1);
    
   
          if(winner(s0, s1)){
            //cout << "Player 1 wins.";
            point2 = 2 + point2;
            player1 = point2;
          }
          if(winner(t0,t1)){
           // cout <<"Player 2 wins.";
            point2 = 2 + point2;
            player2 = point2;
          }
        
        if(pointDouble(s0,s1) < pointDouble(t0,t1)){
         // cout << pointDouble(t0,t1);
          point1 = point1 + 1;
          player2 = point1;
        }

        else if(pointDouble(t0,t1) < pointDouble(s0,s1)){
          //cout << pointDouble(s0, s1);
          point1 = point1 + 1;
          player1 = point1;
        }
    
      cout << endl;
    //cout << s0 << s1 << t0 <<t1 <<endl;
  // cout << "player1 " << player1 << " " << "player2 " << player2 <<endl;
    point1 = 0;
    point2 = 0;
    player1 = 0;
    player2 = 0;
  }

  
}

//dice two players 
// each roll 2 dice
//roll 12 or 21 is highest 

//doubles 11, 22 - ties broken by value 66 highest 
//higest number comes first  in remaining rolls

            