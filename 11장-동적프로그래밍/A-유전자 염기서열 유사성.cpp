/*
	KOREATECH 2021 Algorithm
*/

#include <iostream>
#include <vector>
#include <algorithm>
#define INF 1e9
using namespace std;



struct item {
    int benifit;
    int weight;
};

int main(void) {
    int testcase;
    cin >> testcase;
    while (testcase--) {
        int gap_penalty, mismatch_penalty;
        string word1, word2;
        cin >> gap_penalty >> mismatch_penalty;
        cin >> word1 >> word2;
        vector<vector<int>> dp(word1.size() + 1, vector<int>(word2.size() + 1, INF));
        dp[0][0] = 0;
        for (int i = 1; i < word1.size(); i++)
            dp[i][0] = i * gap_penalty;

        for (int i = 1; i < word2.size(); i++)
            dp[0][i] = i * gap_penalty;

        for (int i = 1; i < word1.size() + 1; i++) {
            for (int j = 1; j < word2.size() + 1; j++) {
                dp[i][j] = min({ dp[i - 1][j - 1] + (word1[i - 1] == word2[j - 1] ? 0 : mismatch_penalty),
                                 dp[i - 1][j] + gap_penalty,
                                 dp[i][j - 1] + gap_penalty });
            }
        }
        cout << dp[word1.size()][word2.size()] << "\n";
    }
}