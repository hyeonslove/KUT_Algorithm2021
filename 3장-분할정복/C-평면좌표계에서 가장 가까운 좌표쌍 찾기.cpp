/*
    KOREATECH 2021 Algorithm
    https://judge.koreatech.ac.kr/problem.php?id=1195

    Nlog(N^2)
*/

#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>

using namespace std;

struct Point {
    int x, y;
};

int dist(Point& p, Point& q) {
    return (p.x - q.x) * (p.x - q.x) + (p.y - q.y) * (p.y - q.y);
}

struct Comp {
    bool comp_in_x;
    Comp(bool b) : comp_in_x(b) {}
    bool operator()(Point& p, Point& q) {
        return (this->comp_in_x ? p.x < q.x : p.y < q.y);
    }
};


int closest_pair(vector<Point>::iterator it, int n) {
    if (n == 2)
        return dist(it[0], it[1]);
    if (n == 3)
        return min({ dist(it[0], it[1]), dist(it[1], it[2]), dist(it[2], it[0]) });

    int line = (it[n / 2 - 1].x + it[n / 2].x) / 2;
    int d = min(closest_pair(it, n / 2), closest_pair(it + n / 2, n - n / 2));

    vector<Point> temp_list;
    temp_list.reserve(n);

    for (int i = 0; i < n; i++) {
        int t = line - it[i].x;
        if (t * t < d)
            temp_list.push_back(it[i]);
    }

    sort(temp_list.begin(), temp_list.end(), Comp(false));

    int mid_size = temp_list.size();
    for (int i = 0; i < mid_size - 1; i++)
        for (int j = i + 1; j < mid_size && (temp_list[j].y - temp_list[i].y) * (temp_list[j].y - temp_list[i].y) < d; j++)
            d = min(d, dist(temp_list[i], temp_list[j]));

    return d;
}


int main(void) {
    int testcase;
    cin >> testcase;
    while (testcase--) {
        int n;
        cin >> n;

        vector<Point> points(n);
        for (auto it = points.begin(); it != points.end(); it++)
            cin >> it->x >> it->y;

        sort(points.begin(), points.end(), Comp(true));
        printf("%.2f\n", sqrt(closest_pair(points.begin(), n)));
    }
}