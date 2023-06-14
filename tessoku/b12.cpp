#include <iostream>
using namespace std;

double N;

bool check(double x) {
    double y = x * x * x + x;

    if(y >= N) {
        return true;
    } else {
        return false;
    }
}

int main() {
    cin >> N;

    double left = 0.0, right = 100000.0;
    while(right - left >= 0.0005) {
        double mid = (left + right) / 2.0;
        if(check(mid)) {
            right = mid;
        } else {
            left = mid + 0.0005;
        }
    }

    cout << left << endl;
    return 0;
}
