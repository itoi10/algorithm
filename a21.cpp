#include <algorithm>
#include <iostream>
using namespace std;

int N, P[2009], A[2009], dp[2009][2009];

void dispDB() {
    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= N; j++) {
            cout << dp[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;
}

int main() {
    cin >> N;
    for(int i = 1; i <= N; i++) {
        cin >> P[i] >> A[i];
    }

    dp[1][N] = 0;
    for(int len = N - 2; len >= 0; len--) {
        for(int l = 1; l <= N - len; l++) {
            int r = l + len;

            int score1 = 0;
            if(l <= P[l - 1] && P[l - 1] <= r) {
                score1 = A[l - 1];
            }

            int score2 = 0;
            if(l <= P[r + 1] && P[r + 1] <= r) {
                score2 = A[r + 1];
            }

            if(l == 1) {
                dp[l][r] = dp[l][r + 1] + score2;
            } else if(r == N) {
                dp[l][r] = dp[l - 1][r] + score1;
            } else {
                dp[l][r] = max(dp[l][r + 1] + score2, dp[l - 1][r] + score1);
            }
            // dispDB();
        }
    }

    int ans = 0;
    for(int i = 1; i <= N; i++) {
        ans = max(ans, dp[i][i]);
    }
    cout << ans << endl;

    return 0;
}
