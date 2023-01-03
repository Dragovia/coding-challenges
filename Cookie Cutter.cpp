#include <iostream>
#include <cmath>
#include <iostream>
#include <iomanip>
using namespace std;
double rad, x,y,h,area,seg;
int main()
{
    double math;
    math = sqrt((x*x) + (y*y));
    cout << fixed << setprecision(4);

    while(cin >> rad >> x >> y){
        if(math >= rad){
            cout << "miss"<<endl;
        }
        else{
             h = rad - sqrt(x * x + y * y);
             area = rad * rad * 3.141592653589793238462643383;
             seg = rad * rad * acos((rad - h) / rad) - (rad - h) * sqrt((2 * rad * h - h * h));
            cout << area - seg << " " << seg << endl;
        }
        }


    return 0;
}
