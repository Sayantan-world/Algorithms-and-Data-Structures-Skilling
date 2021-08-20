#include <bits/stdc++.h>
using namespace std;

// Macros
#define debug(x) cout << '>' << #x << ':' << x << endl;
#define loop0(i,n) for(int i=0; i<(n); i++)
#define loop1(i,n) for(int i=1; i<=(n); i++)
#define fast_io ios_base::sync_with_stdio(false), cin.tie(NULL)
#define ign cin.ignore(numeric_limits<streamsize>::max(),'\n')

#define INF 0x3f3f3f3f
#define PI 3.1415926535897932384626433832795
#define MOD 1000000007
#define endl "\n"
#define fir first
#define sec second
#define pb push_back
#define mp make_pair
#define all(v) (v).begin(), (v).end()
#define dec greater<>()

typedef long long int ll;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<vector<int>> MAT;
typedef vector<ll> VL;
typedef vector<vector<ll>> VVL;
typedef vector<string> VS;
typedef vector<PII> VII;
typedef vector<VI> VVI;
typedef map<int,int> MII;
typedef map<int,int> MCI;
typedef unordered_map<int,int> UMII;
typedef unordered_map<ll,ll> UMLL;
typedef unordered_map<char,int> UMCI;
typedef set<int> SI;
typedef unordered_set<int> USI;
typedef unordered_set<ll> USL;

bool isSameBSTUtil(int a[], int b[], int n, int i1, int i2, int min, int max) {
	
	int j, k;
	for (j = i1; j < n; j++) 
		if (a[j] > min && a[j] < max) break;
	for (k = i2; k < n; k++) 
		if (b[k] > min && b[k] < max) break;
	if (j==n && k==n) return true;
	if (((j==n)^(k==n)) || a[j]!=b[k]) return false;
	return isSameBSTUtil(a, b, n, j+1, k+1, a[j], max) && isSameBSTUtil(a, b, n, j+1, k+1, min, a[j]);
}

bool isSameBST(int a[], int b[], int n) {
	return isSameBSTUtil(a, b, n, 0, 0, INT_MIN, INT_MAX);
}

int main() {
	
	fast_io;
	ll n;
	cin >> n;
    int in[n];
    int post[n];
	for(auto &i: post) cin >> i;
    for(auto &i: in) cin >> i;
    if(isSameBST(in, post, n)) cout << 1 << endl;
    else cout << 0 << endl;
    return 0;
}


