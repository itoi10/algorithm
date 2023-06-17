#include <algorithm>
#include <iostream>
#include <vector>
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
        int r1 = abs(H[i] - H[i - 1]) + dp[i - 1];
        int r2 = abs(H[i] - H[i - 2]) + dp[i - 2];
        dp[i] = min(r1, r2);
    }

    vector<int> route;
    int current = N;

    while(true) {
        // 現在の位置
        route.push_back(current);

        // 最初まで行ったら終了
        if(current == 1) {
            break;
        }

        // どちらのルートが低コストか？
        if(dp[current - 1] + abs(H[current] - H[current - 1]) == dp[current]) {
            current -= 1;
        } else {
            current -= 2;
        }
    }

    reverse(route.begin(), route.end());

    cout << route.size() << endl;
    for(int i = 0; i < route.size(); i++) {
        if(i > 0)
            cout << " ";
        cout << route[i];
    }
    cout << endl;

    return 0;
}
