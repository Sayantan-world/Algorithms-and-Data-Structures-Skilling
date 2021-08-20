#include <bits/stdc++.h>
using namespace std;

// Macros
#define debug(x) cout << '>' << #x << ':' << x << endl;
#define loop0(i,n) for(ll i=0; i<(n); i++)
#define loop1(i,n) for(ll i=1; i<=(n); i++)
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

VL del_k(VL &v, ll k){
	
	/* use Read pointer and Write pointer 
	 * Increase Both read and write pointer if element is NOT k
	 * else increase ONLY Read pointer */
	
	ll rp = 0, wp = 0; 
	ll n = v.size(); 
	loop0(i,n){
		if(v[i] != k){
			v[wp] = v[rp];
			wp++;
			rp++;
		}
		else rp++;
	}
	// Erase the redundant part of the vector
	v.erase (v.begin()+wp, v.end());
	return v;
}  
int main() { 
	
	// Input
	fast_io;
	
    string line;
    ll temp, k;
    VL v;

	getline(cin, line);
	istringstream stream(line);
    while (stream >> temp) v.push_back(temp);
    cin >> k;
    
	
	v = del_k(v, k);
	// Output
	for(auto &i: v) cout << i << " ";
	cout << endl;
} 

