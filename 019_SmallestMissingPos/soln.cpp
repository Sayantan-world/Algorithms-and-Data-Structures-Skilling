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

// Func to calc the smallest positive
int smallest_positive(VI &v, int n){
	
	/*
	 * We know the ans can be in range 1 - N+1
	 * We change all the negative numbers in the array to 1 if 1 is present already else return 1 as ans
	 * Now we update each index by adding n to it
	 * Now if there is an index which is less than n that would be our ans
	*/
	bool flag = true;
	for(int i = 0; i < n; i++){
		if(v[i] == 1){
			flag = false;
		}
	} 
	if(flag) return 1;
	
	for(int i = 0; i < n; i++){
		if(v[i] <= 0 or v[i] > n) v[i] = 1;
	}
	
	
    for (int i = 0; i < n; i++){
		v[(v[i] - 1) % n] += n;
	}
	

	
	for (int i = 0; i < n; i++){
		if (v[i] <= n) return i+1;
	}
	return n+1;

}

int main() { 
	fast_io;
	int n;
	cin >> n;
	VI v;
	string str;
	cin >> str;
	stringstream ss(str);
    // Parse the string
    for (int i; ss >> i;) {
        v.push_back(i);
        if (ss.peek() == ',')
            ss.ignore();
    }
	int ans = smallest_positive(v, n);
	cout << ans << endl;
} 

