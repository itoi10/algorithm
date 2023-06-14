#include <iostream>
using namespace std;

typedef long long int64;
int64 N, K, A[100009];

bool check(int64 x) {
    int64 sum = 0;
    for(int i = 1; i <= N; i++) {
        sum += x / A[i];
    }
    if(sum >= K) {
        return true;
    } else {
        return false;
    }
}

int main() {
    cin >> N >> K;
    for(int i = 1; i <= N; i++)
        cin >> A[i];

    int64 left = 0, right = 1000000000;
    while(left < right) {
        int64 mid = (left + right) / 2;
        if(check(mid)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }

    cout << left << endl;
    return 0;
}
