#include <bits/stdc++.h>
using namespace std;

// Macros
#define debug(x) cout << '>' << #x << ':' << x << endl;
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

void reverse(VL &v){
	
	ll n = v.size();
	// Swap first with last, second with second last and so on -> O(n)
    for (ll i = 0; i < n/2; i++){
		swap(v[i],v[n-i-1]);
    }
}
int main() {
	
	// Input 
	fast_io;
	ll n;
	cin >> n;
    VL v(n);
    for(auto &i: v) cin >> i;
    
    reverse(v);// Reverse Func. call
    
    //Output
	for(auto &i: v) cout << i << " ";
	cout << endl;
} 

