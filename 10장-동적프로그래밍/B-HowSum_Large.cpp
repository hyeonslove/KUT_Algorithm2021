/*
	KOREATECH 2021 Algorithm
*/

#include <iostream>
#include <vector>
using namespace std;

int main(void) {
	int testcase;
	cin >> testcase;
	while (testcase--) {
		int target, length;
		cin >> target >> length;
		vector<int> arr(length);
		vector<bool> dp(target + 1);
		for (int i = 0; i < length; i++) {
			cin >> arr[i];
		}

		dp[0] = true;

		for (int pos = 0; pos < target; pos++) {
			if (dp[pos]) {
				for (auto val : arr) {
					if (val + pos <= target) {
						dp[val + pos] = true;
					}
				}
			}
		}
		if (dp[target]) {
			vector<int> result;
			int pos = target;
			while (pos > 0) {
				for (auto val : arr) {
					if (pos - val < 0)
						continue;
					if (dp[pos - val]) {
						result.push_back(val);
						pos -= val;
						break;
					}
				}
			}
			cout << result.size();
			for (auto i : result) {
				cout << " " << i;
			}
			cout << "\n";
		}
		else {
			cout << "-1" << "\n";
		}
	}
}