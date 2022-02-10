#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int Events;
int dayStart,dayEnd;
int Difference;
int DifferenceAdd=0;

vector<int> vect;


int main() {
  
  int Events;
  cin >> Events;

for(int i = 0; i < Events; i++){
  cin >> dayStart >> dayEnd;


while(dayEnd+1 != dayStart){
  vect.push_back(dayStart);
  dayStart++;

  if((dayEnd+1) == dayStart)
  break;

  
}
}

for(int i =0; i < vect.size(); i++){

}
int k=0;
sort(vect.begin(),vect.end());
cout << endl <<endl;


auto it = std::unique(vect.begin(),vect.begin()+ vect.size());
vect.resize(std::distance(vect.begin(),it));


    cout << vect.size();
return 0;


}
