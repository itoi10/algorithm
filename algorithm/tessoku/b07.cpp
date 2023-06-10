#include <iostream>
using namespace std;

int N, L[500009], R[500009];
int D, B[500009];
int ans[500009];

int main() {
    cin >> D >> N;
    for(int i = 1; i <= N; i++) {
        cin >> L[i] >> R[i];
    }

    // 増減
    for(int i = 1; i <= N; i++) {
        int start = L[i];  // 出勤
        int end = R[i];    // 退勤
        B[start + 1] += 1; // 増加
        B[end + 1] -= 1;   // 減少
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
