#include <bits/stdc++.h>

using namespace std;

void py_print() {
    cout << endl;
}
template<typename T, typename... Args> void py_print(T& arg, Args&... args) {
    cout << arg << " ";
    py_print(args...);
}

#define pp(...) py_print(__VA_ARGS__);


int main() {
    int a = 1;
    string b = "yay";

    pp(a, b);
}
