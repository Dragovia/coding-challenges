#include <bits/stdc++.h>
#include <map>
#include <string>
#include <vector>
#include <iomanip>
#include <iostream>

using namespace std;

 string current;
 string temp;


int main()
{

    vector<string> strs = {"school","schedule","scotland"};


     if(strs.size() == 0)
        return 0;

     current = strs[0];

     for(int i = 0; i < strs.size(); i++){
        temp = "";
        if(current.size() == 0)
                break;

      for(int j = 0; j < i; j++){
        if(j <current.length() && current[j] == strs[i][j]){
        cout << strs[i][j]<<endl;
        temp+= current[j];
      }
       else{
        break;
       }

       current = temp;




      }
      cout<< current;
     }



    return 0;
}

