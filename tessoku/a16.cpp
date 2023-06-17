#include <algorithm>
#include <iostream>
using namespace std;

int N, A[100009], B[100009];
int dp[100009];

int main() {
    cin >> N;
    for(int i = 2; i <= N; i++)
        cin >> A[i];
    for(int i = 3; i <= N; i++)
        cin >> B[i];

    // 動的計画法 O(N)
    // 初手は移動しないので0
    dp[1] = 0;
    // 2つ目は1つ目から移動するのでA[2]
    dp[2] = A[2];
    for(int i = 3; i <= N; i++) {
        // 1つ前から移動する場合と2つ前から移動する場合の小さい方を選ぶ
        int route1 = dp[i - 1] + A[i];
        int route2 = dp[i - 2] + B[i];
        dp[i] = min(route1, route2);
    }

    cout << dp[N] << endl;
    return 0;
}
