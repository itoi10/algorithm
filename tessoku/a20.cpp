// 最長共通部分列
#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

int N, M, dp[2009][2009];
string S, T;

// DP表を表示する
void dispDP() {
    for(int i = 0; i <= N; i++) {
        if(i >= 1) {
            cout << T[i - 1] << " ";
        } else {
            cout << "    ";
        }
    }
    cout << endl;

    for(int i = 0; i <= N; i++) {
        if(i >= 1) {
            cout << S[i - 1] << " ";
        } else {
            cout << "  ";
        }
        for(int j = 0; j <= M; j++) {
            cout << dp[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;
}

int main() {
    cin >> S;
    N = S.size();
    cin >> T;
    M = T.size();

    dp[0][0] = 0;
    for(int i = 0; i <= N; i++) {
        for(int j = 0; j <= M; j++) {
            // 文字が一致した場合は斜め移動回数を+1
            if(i >= 1 && j >= 1 && S[i - 1] == T[j - 1]) {
                dp[i][j] =
                    max(max(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1] + 1);
            } else if(i >= 1 && j >= 1) {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            } else if(i >= 1) {
                dp[i][j] = dp[i - 1][j];
            } else if(j >= 1) {
                dp[i][j] = dp[i][j - 1];
            }

            // debug
            // cout << "i:" << i << " j:" << j << endl;
            // cout << "S:" << S[i - 1] << " T:" << T[j - 1] << endl;
            // dispDP();
        }
    }

    // 斜めに移動した最大回数が答え
    cout << dp[N][M] << endl;

    return 0;
}
