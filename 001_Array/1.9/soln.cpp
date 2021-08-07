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


int main() { 
	
	fast_io;
	ll n;
	cin >> n;
    VL v(n);
    
    ll min = INF;
    ll max = -INF;
    ll total = 0;
	
	for(int i = 0; i < n; i++){
		ll temp;
		cin >> temp;
		if(temp > max) max = temp;
		if(temp < min) min = temp;
		total += temp;
	}
	
	cout << total-(min+max) << endl;
	
} 

