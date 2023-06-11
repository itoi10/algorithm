#include <iostream>
using namespace std;

int N, L[100009], R[100009];
int D, B[100009];
int ans[100009];

int main() {
    cin >> D >> N;
    for(int i = 1; i <= N; i++) {
        cin >> L[i] >> R[i];
    }

    // 前日比
    for(int i = 1; i <= N; i++) {
        int start = L[i]; // 参加日
        int end = R[i];   // 退場日
        B[start] += 1;    // 増加
        B[end + 1] -= 1;  // 減少
    }

    // 累積和
    ans[0] = 0;
    for(int i = 1; i <= D; i++) {
        ans[i] = ans[i - 1] + B[i];
    }

    for(int i = 1; i <= D; i++) {
        cout << ans[i] << endl;
    }

    return 0;
}
