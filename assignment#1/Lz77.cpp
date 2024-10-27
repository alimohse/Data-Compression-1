#include <bits/stdc++.h>
using namespace std;
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;

// #define en endl
#define endl '\n'
#define ll long long
#define all(v) v.begin(), v.end()
#define gofast ios_base::sync_with_stdio(false), cin.tie(nullptr);
// Overloading
istream &operator>>(istream &input, vector<double> &v)
{
    for (auto &it : v)
        input >> it;
    return input;
}
//-------------------------------------------------
// --------------- important functions ---------

int n, m, xv;
int xd[]{1, -1, 0, 0, 1, -1, 1, -1}, yd[]{0, 0, 1, -1, 1, 1, -1, -1};
const int N = 1e5, mod = 1e9 + 7, inf = 0x3f3f3f3f;
const ll llinf = 0x3f3f3f3f3f3f3f3f;
bool checkValidation(int x, int y)
{
    return x >= 0 && x < n && y >= 0 && y < m;
}
struct tag
{
    int position, length;
    char nextc;
};
void solve(string s, int searchwindow, int lookaheadwindow)
{
    int st = 0;
    int length = 0;
    int position = 0;
    vector<tag> vp;
    map<char, vector<int>> mp;
    while (st < s.size())
    {
        if (mp.count(s[st]))
        {
        }
    }
}

int main()
{
    gofast
        // cout << fixed << setprecision(10);
        int T = 1;
    cin >> T;
    // seive();
    // build();
    while (T--)
    {
        solve();
    }
    return 0;
}