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
typedef vector<vector<long>> VVL;
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

void leftRotate(VI &v, int k) {
    // ( xR yR )R  = y x
    
	VI v1 (v.begin(), v.begin()+k); // x
	VI v2 (v.begin()+k, v.end()); // y
	
	reverse(v1.begin(), v1.end()); // xR
	reverse(v2.begin(), v2.end()); // yR
	
	v1.insert(v1.end(), v2.begin(), v2.end()); // (xR yR)
	
	v = v1;
	
	reverse(v.begin(), v.end()); // (xR yR)R = y x
} 
  
int main() { 
	fast_io;
	int n, k;
	cin >> n;
    VI v(n);
    for(auto &i: v) cin >> i;
    cin >> k;
    k = k % n;
    k = n - k;
    leftRotate(v, k);
    for(auto &i: v) cout << i << " ";
    cout << endl;
} 

