#include <bits/stdc++.h>

using namespace std;

int gen_vec() {
    return 0;
}
template<typename Dim, typename... Dims> auto gen_vec(Dim& dim, Dims&... dims) {
    auto invec gen_vec(dims...);

    decltype(gen_vec)(a, invec) vec;

    return vec;
}

#define vec(type, ...) gen_vec(__VA_ARGS__);

int main() {
    vec(2, 3);
}
