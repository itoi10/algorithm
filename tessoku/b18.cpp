#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int N, S, A[69];
bool dp[69][100009]; // [カード枚数][合計値]

int main() {
    cin >> N >> S;
    for(int i = 1; i <= N; i++)
        cin >> A[i];

    // 0段目
    dp[0][0] = true; // 0は0枚で作れる
    for(int i = 1; i <= S; i++)
        dp[0][i] = false;

    // 1段目以降
    for(int i = 1; i <= N; i++) {
        // i番目のカードまでで作れる合計値
        for(int j = 0; j <= S; j++) {
            // jがA[i]より小さい場合はi番目のカードを使えない
            if(j < A[i]) {
                // 上の段の結果を反映
                dp[i][j] = dp[i - 1][j];
                // jがA[i]以上の場合はi番目のカードを使える
            } else {
                // i番目のカードを使う場合と使わない場合のどちらかがtrueならtrue
                dp[i][j] = dp[i - 1][j] || dp[i - 1][j - A[i]];
            }
        }
    }

    // 答えを満たさない場合は-1
    if(!dp[N][S]) {
        cout << -1 << endl;
        return 0;
    }

    vector<int> ans;
    int current = S;

    for(int i = N; i >= 1; i--) {
        // i番目のカードを使わない場合
        if(dp[i - 1][current]) {
            continue;
        }
        // i番目のカードを使う場合
        ans.push_back(i);
        // 合計値からi番目のカードの値を引く
        current -= A[i];
    }

    reverse(ans.begin(), ans.end());

    cout << ans.size() << endl;
    for(int i = 0; i < ans.size(); i++) {
        if(i > 0)
            cout << " ";
        cout << ans[i];
    }
    cout << endl;

    return 0;
}
