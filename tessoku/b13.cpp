#include <iostream>
using namespace std;
typedef long long int64;

int N, K;
int A[100009], R[100009];

int main() {
    cin >> N >> K;
    for(int i = 1; i <= N; i++) {
        cin >> A[i];
    }

    // 累積和
    int sum[100009];
    sum[0] = 0;
    for(int i = 1; i <= N; i++) {
        sum[i] = sum[i - 1] + A[i];
    }

    // // 表示
    // for(int i = 0; i <= N; i++) {
    //     cout << sum[i] << " ";
    // }
    // cout << endl;

    // 尺取り法 O(N)
    for(int i = 1; i <= N; i++) {
        if(i == 1)
            R[i] = 0;
        else
            R[i] = R[i - 1];

        while(R[i] < N && sum[R[i] + 1] - sum[i - 1] <= K) {
            R[i] += 1;
        }
    }
    int64 ans = 0;
    for(int i = 1; i <= N; i++) {
        ans += (R[i] - i + 1);
    }

    cout << ans << endl;

    return 0;
}
