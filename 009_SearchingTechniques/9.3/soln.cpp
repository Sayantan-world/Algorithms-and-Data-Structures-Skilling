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

ll interpolationSearch(ll sortedArray[], ll toFind, ll len) {
	
	if(len == 1 && toFind == sortedArray[0]) return 0; // Extreme case
    ll low = 0;
    ll high = len - 1;
    ll mid;

    ll l = sortedArray[low];
    ll h = sortedArray[high];

    while (l <= toFind && h >= toFind) {
        ll high_low = (high - low);
        ll toFind_l = (toFind - l);
        ll product = high_low*toFind_l;
        ll h_l = h-l;
        ll step = product / h_l;
        mid = low + step;
        ll m = sortedArray[mid];

        if (m < toFind) {
            l = sortedArray[low = mid + 1];
        } else if (m > toFind) {
            h = sortedArray[high = mid - 1];
        } else {
            return mid;
        }
    }

    if (sortedArray[low] == toFind)
        return low;
    else
        return -1; // Not found
}
int main() { 
	
	fast_io;
	ll n;
	cin >> n;
	ll arr[n];
	for(ll i = 0; i < n; i++){
		ll temp;
		cin >> temp;
		arr[i] = temp;
	}
	ll k;
	cin >> k;
	cout << interpolationSearch(arr, k, n) << endl;
	
} 

