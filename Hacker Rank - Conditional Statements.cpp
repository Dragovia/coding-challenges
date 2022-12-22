#include <bits/stdc++.h>
#include <map>
#include <string>
using namespace std;

string ltrim(const string &);
string rtrim(const string &);



int main()
{
    string n_temp;
    getline(cin, n_temp);
     map<string, string> gquiz1;

    int n = stoi(ltrim(rtrim(n_temp)));

    // insert elements in random order
    gquiz1.insert(pair<string, string>("1", "one"));
    gquiz1.insert(pair<string, string>("2", "two"));
    gquiz1.insert(pair<string, string>("3", "three"));
    gquiz1.insert(pair<string, string>("4", "four"));
    gquiz1.insert(pair<string, string>("5", "five"));
    gquiz1.insert(pair<string, string>("6", "six"));
    gquiz1.insert(pair<string, string>("7", "seven"));
    gquiz1.insert(pair<string, string>("8", "eight"));
    gquiz1.insert(pair<string, string>("9", "nine"));


    map<string, string>::iterator itr;

    if(gquiz1.find(n_temp) == gquiz1.end()){
      cout << "Greater than 9" << endl;
    }else{
      cout << gquiz1.find(n_temp)->second;
    }

    // for(itr = gquiz1.begin(); itr != gquiz1.begin(); ++itr) {
    //     if( itr->first == n_temp)
    //     {
    //         cout <<itr-> second ;
    //         break;
    //     }

    //    else if (itr->first != n_temp && itr == gquiz1.end()){
    //        cout << "Greater than 9";
    //         break;
    //     }
    // }



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
