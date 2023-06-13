#include <algorithm>
#include <iostream>
using namespace std;

int N, A[100009];
int Q, X[100009];

int search(int x) {
    int pos = lower_bound(A + 1, A + N + 1, x) - A - 1;
    return pos;
}

int main() {
    cin >> N;
    for(int i = 1; i <= N; i++)
        cin >> A[i];

    cin >> Q;
    for(int i = 1; i <= Q; i++)
        cin >> X[i];

    // 二分探索のためソート
    sort(A + 1, A + N + 1);

    for(int i = 1; i <= Q; i++) {
        int ans = search(X[i]);
        cout << ans << endl;
    }

    return 0;
}
