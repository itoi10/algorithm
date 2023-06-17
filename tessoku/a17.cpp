#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int N, A[100009], B[100009], dp[100009];

int main() {
    cin >> N;
    for(int i = 2; i <= N; i++)
        cin >> A[i];
    for(int i = 3; i <= N; i++)
        cin >> B[i];

    // 動的計画法
    dp[1] = 0;
    dp[2] = A[2];
    for(int i = 3; i <= N; i++) {
        int r1 = dp[i - 1] + A[i];
        int r2 = dp[i - 2] + B[i];
        dp[i] = min(r1, r2);
    }

    // ルートの復元
    vector<int> route;
    // 最後からスタート
    int current = N;

    while(true) {
        // 位置を記録
        route.push_back(current);
        // 最初まで戻ったら終了
        if(current == 1)
            break;

        // 1手戻るのが最短か？
        if(dp[current - 1] + A[current] == dp[current]) {
            current -= 1;
        } else {
            // 2手戻るのが最短
            current -= 2;
        }
    }

    // 逆順にする
    reverse(route.begin(), route.end());

    // 手数とルートを出力
    cout << route.size() << endl;
    for(int i = 0; i < route.size(); i++) {
        if(i > 0)
            cout << " ";
        cout << route[i];
    }

    cout << endl;
    return 0;
}
