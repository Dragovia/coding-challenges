#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n;
    int numbers;
    vector<int> numb;


    cin >>n;

    int counter =1;

    for(int i = 0; i < n; i++){
        cin>> numbers;
        numb.push_back(numbers);
    }

    int lastElement = numb[numb.size()-1];
    bool notFound;

    for(int i = 1; i < lastElement; i++){
       int temp = i;
    bool notFound = true;

       for(int j = 0; j < numb.size()-1; j++){
         if(temp ==numb[j])
            notFound = false;
            counter++;
            //cout << counter++;
       }


       if(notFound){
        if(i < lastElement) cout << temp<<endl;
        else cout << temp;

       }

    }

    if(n == 1 && counter == 1 && numbers ==1){
        cout << "good job";
    }


    if(counter-1 == ((n-1)*(n-1)) && counter!=1 ){

        cout << "good job";
    }
