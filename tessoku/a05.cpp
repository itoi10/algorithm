#include <iostream>
using namespace std;

int q1(int N, int K) {
    // 全探索 O(N^3)
    int ans = 0;
    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= N; j++) {
            for(int k = 1; k <= N; k++) {
                if(i + j + k == K) {
                    ans += 1;
                }
            }
        }
    }

    return ans;
}

int q2(int N, int K) {
    // 全探索 O(N^2)
    int ans = 0;
    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= N; j++) {
            int k = K - i - j;
            if(k >= 1 && k <= N) {
                ans += 1;
            }
        }
    }

    return ans;
}

int main() {
    int N, K;
    cin >> N >> K;

    int ans = q2(N, K);

    cout << ans << endl;
}
