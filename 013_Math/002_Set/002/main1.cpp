//
// 数の合併 (A ∪ B)
//
// https://algo-method.com/tasks/590

/* -------------------------------------------------------------------------- */

#include <bits/stdc++.h>

using namespace std;
using ll = long long;

#define rep(i, a, b)            for (int i = (a); i < (b); i++)
#define rrep(i, b, a)           for (int i = (b); (a) < i; i--)
#define vec1t(t)                vector<t>
#define vec2t(t)                vector<vector<t>>
#define vec3t(t)                vector<vector<vector<t>>>
#define vec1v(n, t, a, v)       vec1t(t) n(a, v)
#define vec2v(n, t, a, b, v)    vec2t(t) n(a, vec1t(t)(b, v))
#define vec3v(n, t, a, b, c, v) vec3t(t) n(a, vec2t(t)(b, vec1t(t)(c, v)))
#define all(n)                  n.begin(),n.end()
#define rall(n)                 n.rbegin(),n.rend()
#define pii                     pair<int, int>
#define pll                     pair<ll, ll>

#define printVec1(n)            rep(i, 0, (int)(n).size()) {if (i) cout << " ";cout << (n)[i];}cout << endl;
#define printVec2(n)            rep(j, 0, (int)(n).size()) {printVec1((n)[j]);}
#define printYesNo(f)           if (f) cout << "Yes" << endl; else cout << "No" << endl;

const ll MOD9 = 1e9+9;
const ll MOD7 = 1e9+7;
const ll MOD3 = 998244353;

/* -------------------------------------------------------------------------- */

void solve()
{
  // [ input ]
  int N, M; cin >> N >> M;
  vec1v(A, int, N, 0); rep(i, 0, N) cin >> A[i];
  vec1v(B, int, M, 0); rep(i, 0, M) cin >> B[i];

  // [ simulate ]
  // < create hist table >
  int maxA = *max_element(all(A));
  int maxB = *max_element(all(B));
  int maxAB = max(maxA, maxB);
  vec1v(H, int, maxAB+1, 0);
  for (auto a : A) H[a]++;
  for (auto b : B) H[b]++;

  // [ output ]
  for (int i = 0; i <= maxAB; i++)
    if (H[i] != 0)
      cout << i << endl;
}

/* -------------------------------------------------------------------------- */

int main()
{
  #ifndef TDD
    // [ submit mode ]
    solve();
  #else
    // [ test mode ]
    // set I/O
    freopen("input.txt",  "r",  stdin);
    freopen("output.txt", "w", stdout);
    // test samples
    int times;
    cin >> times;
    for(int i = 1; i <= times; i++) {
      cout << "[ sample: " << i << " ]" << endl;
      clock_t start = clock();
      solve();
      clock_t end = clock();
      cout << fixed
          << "(Run Time: " << ((double)(end - start) / CLOCKS_PER_SEC) * 1000 << " ms)"
          << endl << endl;
    }
  #endif
  return (0);
}