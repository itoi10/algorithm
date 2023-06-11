/*
典型 001 https://atcoder.jp/contests/typical90/tasks/typical90_a

g++ q1.cpp; ./a.out < inputs/q01.txt

入力例
---
3 34
1
8 13 26
*/

#include <iostream>
#include <vector>
using namespace std;

// Lを長さM以上のピースに分解できるか判定
bool solve(int M, int N, int L, int K, vector<int> A) {
    int cnt = 0;
    int pre = 0;
    for (int i=0; i<N; i++) {
        if(A.at(i) - pre >= M && L - A.at(i) >= M) {
            cnt += 1;
            pre = A.at(i);
        }
    }
    if (cnt >= K) {
        return true;
    }
    return false;
}

int main() {
    // 入力値
    int N, L, K;
    cin >> N >> L >> K;
    vector<int> A(N);
    for (int i=0; i<N; i++) {
        cin >> A.at(i);
    }

    // 二分法
    int left = -1;
    int right = L + 1;

    while (right - left > 1) {
        int mid = left + (right - left) / 2;
        if (solve(mid, N, L, K, A)) {
            left = mid;
        } else {
            right = mid;
        }
    }
    
    // 解
    cout << left << endl;

    return 0;
}