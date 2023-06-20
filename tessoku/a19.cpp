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

    // 小さい値で初期化
    for(int i = 0; i <= N; i++)
        for(int j = 0; j <= W; j++)
            dp[i][j] = -1'000'000'000'000'000LL;

    /*動的計画法 O(NW)

    no,weight,value
    3,13
    3,17
    5,29
    1,10

    no\wight | 0  1  2  3  4  5  6  7
    ---------+-----------------------
    0        | 0  x  x  x  x  x  x  x
    1        | 0  x  x 13  x  x  x  x
    2        | 0  x  x 17  x  x 30  x
    3        | 0  x  x 17  x 29 30  x
    4        | 0 10  x 17 27 29 30 40
    */
    dp[0][0] = 0;
    // アイテム1番目からN番目まで
    for(int i = 1; i <= N; i++) {
        // 重さ0からWまで
        for(int weight = 0; weight <= W; weight++) {
            // 使える重さがアイテムの重さより小さい場合
            if(weight < w[i]) {
                // アイテムを使えないので上の行の値をそのままコピー
                dp[i][weight] = dp[i - 1][weight];
            }
            // 使える重さがアイテムの重さ以上の場合
            else {
                // アイテムを使わない場合. 上の行の値をそのままコピー
                int64 notUse = dp[i - 1][weight];
                // アイテムを使う場合. アイテムを使った場合の価値を計算
                int64 use = dp[i - 1][weight - w[i]] + v[i];
                // 価値が大きい方を選択
                dp[i][weight] = max(notUse, use);
            }
        }
    }

    int64 ans = 0;
    for(int i = 0; i <= W; i++)
        ans = max(ans, dp[N][i]);

    cout << ans << endl;

    return 0;
}
