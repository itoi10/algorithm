#include <iostream>
using namespace std;

int A, B;
bool Answer = false;

int main() {
    cin >> A >> B;
    // A以上B以下の整数のうち、100の約数があるか判定する
    for(int i = A; i <= B; i++) {
        if(100 % i == 0) {
            Answer = true;
            break;
        }
    }

    if(Answer)
        cout << "Yes" << endl;
    else
        cout << "No" << endl;
}
