#include <algorithm>
#include <iostream>
using namespace std;

int N, A[100009], P[100009], Q[100009];
int D, L[100009], R[100009];

int main() {
    cin >> N;
    for(int i = 1; i <= N; i++)
        cin >> A[i];
    cin >> D;
    for(int i = 1; i <= D; i++)
        cin >> L[i] >> R[i];

    // // O(N * D)
    // for(int i = 1; i <= D; i++) {
    //     int ans = 0;
    //     for(int j = 1; j <= N; j++) {
    //         if(L[i] <= j && j <= R[i])
    //             continue;
    //         ans = max(ans, A[j]);
    //     }
    //     cout << ans << endl;
    // }

    // 累積和 O(N)
    // 前から見たときの最大値
    P[1] = A[1];
    for(int i = 2; i <= N; i++)
        P[i] = max(P[i - 1], A[i]);

    // 後ろから見たときの最大値
    Q[N] = A[N];
    for(int i = N - 1; i >= 1; i--)
        Q[i] = max(Q[i + 1], A[i]);

    // 大きい方を出力
    for(int i = 1; i <= D; i++)
        cout << max(P[L[i] - 1], Q[R[i] + 1]) << endl;

    return 0;
}
