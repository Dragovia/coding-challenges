#include <bits/stdc++.h>
#include <map>
#include <string>
using namespace std;

string ltrim(const string &);
string rtrim(const string &);



int main()
{
    string n_temp;
    //getline(cin, n_temp);
    int burrito;
   // cin >> burrito;
   int dork;
   int temp;
   cin >> n_temp >> burrito;
     map<int, string> gquiz1;
    temp = burrito;
    int n = stoi(ltrim(rtrim(n_temp)));
    int counter =0;
    dork = burrito - 9;

    // insert elements in random order
    gquiz1.insert(pair<int, string>(1, "one"));
    gquiz1.insert(pair<int, string>(2, "two"));
    gquiz1.insert(pair<int, string>(3, "three"));
    gquiz1.insert(pair<int, string>(4, "four"));
    gquiz1.insert(pair<int, string>(5, "five"));
    gquiz1.insert(pair<int, string>(6, "six"));
    gquiz1.insert(pair<int, string>(7, "seven"));
    gquiz1.insert(pair<int, string>(8, "eight"));
    gquiz1.insert(pair<int, string>(9, "nine"));



    map<int, string>::iterator itr;

    /*if(gquiz1.find(n_temp) == gquiz1.end()){
      cout << "Greater than 9" << endl;
    }else{
      cout << gquiz1.find(n_temp)->second;
    }


*/


cout << temp << " lol"<<endl;

     for(itr = gquiz1.begin(); itr != gquiz1.end(); ++itr) {


         if( itr->first == n)
         {
             cout <<itr-> second<<endl;
             n++;


            // counter++;
         }

          if(temp < 9){
              temp = temp - 1;
            cout << temp << "bro wtf/n";
            while(temp =0)
                break;
          }


    /*  else if (itr->first != n_temp && itr == gquiz1.end()){
        cout << "Greater than 9";
             break;
         }*/



     }


 for(int i = 0; i <dork; i++){
            if(i % 2 == 0){
                cout <<"even"<<endl;
            }
            else if( i % 2 != 0){
                cout <<"odd"<<endl;
            }
         }



    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
