//
// Q3. 人気者の友達
//
// https://algo-method.com/tasks/673

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

const ll MOD9 = 1e9+9;
const ll MOD7 = 1e9+7;
const ll MOD3 = 998244353;

/* -------------------------------------------------------------------------- */

void solve()
{
  // [ input ]
  int N, M; cin >> N >> M;

  // [ create graph ]
  vec2t(int) graph(N);
  rep(_, 0, M) {
    int a, b; cin >> a >> b;
    graph[a].push_back(b);
    graph[b].push_back(a);
  }

  // [ find strudent ]
  int maxF = 0;
  int maxI = -1;
  rep(i, 0, N) {
    if (maxF < graph[i].size()) {
      maxF = (int)graph[i].size();
      maxI = i;
    }
  }

  // [ output ]
  sort(all(graph[maxI]));
  rep(j, 0, (int)graph[maxI].size()) {
    if (j) cout << " ";
    cout << graph[maxI][j];
  }
  cout << endl;
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