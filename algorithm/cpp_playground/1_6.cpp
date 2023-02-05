#include <algorithm>
#include <cstdio>
using namespace std;

// 全探索
void solve() {
    // input
    int n = 5;
    int a[] = {2, 3, 4, 5, 10};

    int ans = 0;

    for(int i = 0; i < n; i++) {
        for(int j = i + 1; j < n; j++) {
            for(int k = j + 1; k < n; k++) {
                int len = a[i] + a[j] + a[k];
                int ma = max(a[i], max(a[j], a[k]));
                int rest = len - ma;

                if(ma < rest) {
                    ans = max(ans, len);
                }
            }
        }
    }

    printf("%d\n", ans);
}

int main() {

    solve();

    return 0;
}
