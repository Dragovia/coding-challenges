#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int n;
    int k;
    float total;
    int range;
    float bestcase,worstcase;
    cin >> n >> k;
     int missing = n-k;
    for(int i = 0; i < k; i++){

        cin >> range;
        total = total + range;
    }

     bestcase = (total+(missing) * 3)/n;
     worstcase = (total - (missing) * 3)/n;

     cout << worstcase << " " << bestcase;
}

