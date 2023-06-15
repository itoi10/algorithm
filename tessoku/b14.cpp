#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
typedef long long int64;

int64 N, K, A[109];

// ビット全探索
vector<int64> Enumerate(vector<int64> A) {
    vector<int64> sumList;

    for(int i = 0; i < (1 << (int)A.size()); i++) {
        int64 sum = 0;
        for(int j = 0; j < (int)A.size(); j++) {
            if((i / (1 << j)) % 2 == 1) {
                sum += A[j];
            }
        }
        sumList.push_back(sum);
    }
    return sumList;
}

int main() {
    cin >> N >> K;
    for(int i = 1; i <= N; i++)
        cin >> A[i];

    // 半分に分ける
    vector<int64> L1, L2;
    for(int i = 1; i <= N / 2; i++)
        L1.push_back(A[i]);
    for(int i = N / 2 + 1; i <= N; i++)
        L2.push_back(A[i]);

    // 半分に分けたそれぞれの部分集合の和を列挙
    vector<int64> sum1 = Enumerate(L1);
    vector<int64> sum2 = Enumerate(L2);
    sort(sum1.begin(), sum1.end());
    sort(sum2.begin(), sum2.end());

    // 二分探索
    for(int i = 0; i < (int)sum1.size(); i++) {
        int pos =
            lower_bound(sum2.begin(), sum2.end(), K - sum1[i]) - sum2.begin();
        if(pos < (int)sum2.size() && sum2[pos] == K - sum1[i]) {
            cout << "Yes" << endl;
            return 0;
        }
    }

    cout << "No" << endl;
    return 0;
}
