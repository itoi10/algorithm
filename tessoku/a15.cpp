#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N, A[100009], B[100009];
    cin >> N;
    for(int i = 1; i <= N; i++) {
        cin >> A[i];
    }

    // Aをソートし重複削除した配列Tを作成
    vector<int> T;
    for(int i = 1; i <= N; i++) {
        T.push_back(A[i]);
    }
    sort(T.begin(), T.end());
    T.erase(unique(T.begin(), T.end()), T.end());

    // A[i]がAの中で何番目に小さいかをB[i]に格納
    for(int i = 1; i <= N; i++) {
        B[i] = lower_bound(T.begin(), T.end(), A[i]) - T.begin() + 1;
    }

    for(int i = 1; i <= N; i++) {
        if(i > 1) {
            cout << " ";
        }
        cout << B[i];
    }

    return 0;
}
