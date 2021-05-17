/*
	KOREATECH 2021 Algorithm
*/

#include <iostream>
#include <vector>
using namespace std;

typedef long long ll;

int main(void) {
    int testcase;
    cin >> testcase;
    while (testcase--) {
        int target, length;
        cin >> target >> length;
        vector<int> arr(length);
        vector<ll> dp(target + 1);
        for (int i = 0; i < length; i++) {
            cin >> arr[i];
        }

        dp[0] = 1;

        for (int pos = 0; pos < target; pos++) {
            if (dp[pos]) {
                for (auto val : arr) {
                    if (val + pos <= target) {
                        dp[val + pos] += dp[pos];
                    }
                }
            }
        }
        cout << dp[target] << "\n";
    }
}