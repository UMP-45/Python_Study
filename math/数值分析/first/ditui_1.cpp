#include<iostream>
#include<vector>
//#include <iomanip>

int main(void){
int k = 0;
double n = 0;
long double t = 0.0953102;

using std::cin;
using std::endl;
using std::cout;

cin >> n;

using std::vector;
vector<double> y(n);
y[0] = t;
cout << y[0] << endl;
for(long double i = 0; i < n-1; ++i){
    ++k;
    y[i+1] = 1/(i+1) - 10*y[i];    
}

/* y[1] = 1 - 10*y[0];
y[2] = 0.5 - 10*y[1]; */
/* int  i = 2;
i = 1/i; */

using std::setprecision;
using std::fixed;
cout << "K = " << k << endl;
for(auto i = 0; i < n; ++i) cout << "i:" <<  i << "    " << y[i] << endl;


//cout << fixed << setprecision(7) << t+t <<endl;
}
