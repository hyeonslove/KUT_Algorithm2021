/*
	KOREATECH 2021 Algorithm
	https://judge.koreatech.ac.kr/problem.php?id=1196
*/

#include <iostream>
#include <vector>
#include <random>
using namespace std;

void findMinMax(vector<int> arr, int n, int* min, int* max) {
	int i, small, large;
	*min = arr[0];
	*max = arr[0];
	for (i = 0; i < n - 1; i += 2) {
		if (arr[i] < arr[i + 1]) {
			small = arr[i];
			large = arr[i + 1];
		}
		else {
			large = arr[i];
			small = arr[i + 1];
		}
		if (small < *min)
			*min = small;
		if (large > * max)
			*max = large;
	}
	if (n % 2 == 1) {
		if (arr[n - 1] < *min)
			*min = arr[n - 1];

		if (arr[n - 1] > * max)
			*max = arr[n - 1];
	}
}

int main(void) {
	int testcase;
	cin >> testcase;
	while (testcase--) {
		int data_length;
		cin >> data_length;
		vector<int> v;
		for (int i = 0; i < data_length; i++) {
			int input_data;
			cin >> input_data;
			v.push_back(input_data);
		}
		int max = 0, min = 0;
		findMinMax(v, data_length, &min, &max);

		cout << max << " " << min << "\n";
	}
}