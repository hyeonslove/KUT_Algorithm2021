/*
	KOREATECH 2021 Algorithm
*/

#include <iostream>
#include <vector>
#include <algorithm>
#define INF 1e9
using namespace std;

typedef long long ll;


int main(void) {
    int testcase;
    cin >> testcase;
    while (testcase--) {
        int target, length;
        cin >> target >> length;
        vector<int> arr(length);
        vector<vector<int>> dp(target + 1, vector<int>(NULL, NULL));
        for (int i = 0; i < length; i++)
            cin >> arr[i];

        dp[0].push_back(NULL);

        for (int pos = 0; pos < target; pos++) {
            if (dp[pos].size() != 0) {
                for (auto val : arr) {
                    if (val + pos <= target) {
                        // 값이 아무것도 없으면 현재 자신의 값 + 새로운 값을 추가시킴
                        if (dp[val + pos].size() == 0) {
                            for (auto val1 : dp[pos])
                                dp[val + pos].push_back(val1);

                            dp[val + pos].push_back(val);
                        }
                        else {
                            // 값이 존재하면 무엇이 더 짧은지 비교하고
                            if (dp[val + pos].size() > dp[pos].size() + 1) {
                                dp[val + pos].clear();
                                for (auto val1 : dp[pos])
                                    dp[val + pos].push_back(val1);

                                dp[val + pos].push_back(val);
                            }
                        }
                    }
                }
            }
        }
        if (dp[target].size() != 0) {
            cout << dp[target].size() - 1;
            for (auto iter = dp[target].begin() + 1; iter != dp[target].end(); iter++) {
                cout << " " << *iter;
            }
        }
        else {
            cout << "-1";
        }
        cout << "\n";
    }
}