/*
    KOREATECH 2021 Algorithm
    https://judge.koreatech.ac.kr/problem.php?id=1191

    해당 문제는 교수님이 제시하신 것의 다른 방법으로 진행해야함.
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Result {
public:
    int number;
    int counting;
};

int main()
{
    int testcase;
    cin >> testcase;

    while (testcase--) {
        Result res, counter;
        vector<int> v;

        int length;
        cin >> length;
        for (int i = 0; i < length; i++) {
            int temp;
            cin >> temp;
            v.push_back(temp);
        }
        if (v.size() != 1) {
            sort(v.begin(), v.end());

            res.number = 0; res.counting = 0;
            counter.number = v[0]; counter.counting = 1;
            for (int i = 1; i < length; i++) {
                if (v[i] == counter.number) {
                    counter.counting++;
                }
                else {
                    if (counter.counting > res.counting) {
                        res.number = counter.number;
                        res.counting = counter.counting;
                    }
                    counter.number = v[i];
                    counter.counting = 1;
                }
            }
            if (counter.counting > res.counting) {
                cout << counter.number << "\n";
            }
            else {
                cout << res.number << "\n";
            }
        }
        else {
            cout << v[0] << "\n";
        }
    }
}