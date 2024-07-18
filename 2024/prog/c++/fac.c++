#include <bits/stdc++.h>

using namespace std;

int fac() {
    return 1;
}
template<typename T> int fac(T n) {
    if (n > 0)
        return n * fac(n-1);
    else
        return fac();
}

int main() {
    cout << fac(6);
}
