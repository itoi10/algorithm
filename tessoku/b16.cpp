#include <algorithm>
#include <iostream>
using namespace std;

int N, H[100009];
int dp[100009];

int main() {
    cin >> N;
    for(int i = 1; i <= N; i++)
        cin >> H[i];

    // 初手は0
    dp[1] = 0;
    // 2つ目は1つ目から移動する1手
    dp[2] = abs(H[2] - H[1]);
    for(int i = 3; i <= N; i++) {
        // １つ前から移動する場合と2つ前から移動する場合の小さい方を選ぶ
        int route1 = abs(H[i] - H[i - 1]) + dp[i - 1];
        int route2 = abs(H[i] - H[i - 2]) + dp[i - 2];
        dp[i] = min(route1, route2);
    }

    cout << dp[N] << endl;
    return 0;
}
