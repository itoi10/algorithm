#include <iostream>
#include <string>
using namespace std;

int main() {
    string N;
    int ans = 0;
    cin >> N;

    // N(2進数)を10進数に変換する
    for(int i = 0; i < N.size(); i++) {
        int powerOf2 = (1 << i);
        int bit = 0;
        if(N[N.size() - 1 - i] == '1')
            bit = 1;
        ans += powerOf2 * bit;
    }
    cout << ans << endl;
    return 0;
}
