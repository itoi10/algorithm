#include <algorithm>
#include <iostream>
using namespace std;
typedef long long int64;

int64 N, W, w[109], v[109];
int64 dp[109][100009];

int main() {
    cin >> N >> W;
    for(int i = 1; i <= N; i++)
        cin >> w[i] >> v[i];

    // 大きい値で初期化
    for(int i = 0; i <= N; i++)
        for(int j = 0; j <= 100000; j++)
            dp[i][j] = 1'000'000'000'000'000LL;

    // weightが大きくvalueが小さいのでループカウンタはvalueにする
    dp[0][0] = 0;
    for(int i = 1; i <= N; i++) {
        for(int value = 0; value <= 100000; value++) {
            if(value < v[i]) {
                // 上の行の値をそのままコピー
                dp[i][value] = dp[i - 1][value];
            } else {
                // 軽い方を選択
                dp[i][value] =
                    min(dp[i - 1][value], dp[i - 1][value - v[i]] + w[i]);
            }
        }
    }

    int64 ans = 0;
    for(int i = 0; i <= 100000; i++)
        // 重さがW以下の中で最大の価値を探す
        if(dp[N][i] <= W)
            ans = i;

    cout << ans << endl;

    return 0;
}
