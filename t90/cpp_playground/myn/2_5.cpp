#include <algorithm>
#include <iostream>

using namespace std;
static const int MAX = 200000;

int main() {
    int R[MAX], n;

    // input
    cin >> n;
    for(int i = 0; i < n; i++) {
        cin >> R[i];
    }

    // 初期値 (十分小さい値)
    int maxv = -2000000000;
    // 一番最初の値を最小値とする
    int minv = R[0];

    for(int i = 1; i < n; i++) {
        // 最大値を更新
        maxv = max(maxv, R[i] - minv);
        // 最小値を保持
        minv = min(minv, R[i]);
    }

    cout << maxv << endl;

    return 0;
}
