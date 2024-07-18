#include <bits/stdc++.h>
using namespace std;


int main() {
    vector<int> vec = {1, 2, 3, 4, 5, 6, 7, 8, 0, -2, 4};

    sort(begin(vec), end(vec), [](int a, int b) {return a>b;});

    for (auto i: vec)
        cout << i << endl;

}
