#include <iostream>
using namespace std;
typedef long long int64;

int N, K;
int A[100009], R[100009];

// 全探索 O(N^2) TLE
int64 fullSearch() {
    int64 ans = 0;

    for(int i = 1; i < N; i++) {
        for(int j = i + 1; j <= N; j++) {
            if(A[j] - A[i] <= K)
                ans += 1;
        }
    }
    return ans;
}

// 尺取り法 O(N)
int64 syakutori() {
    for(int i = 1; i <= N - 1; i++) {
        if(i == 1)
            R[i] = 1;
        else
            R[i] = R[i - 1];

        while(R[i] < N && A[R[i] + 1] - A[i] <= K) {
            R[i] += 1;
        }
    }
    int64 ans = 0;
    for(int i = 1; i <= N - 1; i++) {
        ans += (R[i] - i);
    }
    return ans;
}

int main() {
    cin >> N >> K;
    for(int i = 1; i <= N; i++) {
        cin >> A[i];
    }

    // cout << fullSearch() << endl;
    cout << syakutori() << endl;

    return 0;
}
