/*
	KOREATECH 2021 Algorithm
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long ll;

struct item {
    int benifit;
    int weight;
};

int main(void) {
    int testcase;
    cin >> testcase;
    while (testcase--) {
        int bag, cnt;
        cin >> bag >> cnt;
        vector<vector<int>> dp(cnt + 1, vector<int>(bag + 1, 0));
        vector<item> list(cnt);
        for (int i = 0; i < cnt; i++)
            cin >> list[i].benifit >> list[i].weight;

        for (int i = 1; i <= cnt; i++) {
            for (int x = 0; x <= bag; x++) {
                if (list[i - 1].weight > x) {
                    dp[i][x] = dp[i - 1][x];
                }
                else {
                    dp[i][x] = max(dp[i - 1][x], dp[i - 1][x - list[i - 1].weight] + list[i - 1].benifit);
                }
            }
        }

        cout << dp[cnt][bag] << "\n";
    }

}