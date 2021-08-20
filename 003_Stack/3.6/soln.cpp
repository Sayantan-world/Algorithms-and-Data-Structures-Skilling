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


int countRev(string expr) {
	
    int l = expr.length();
    if (l % 2) return -1;
    
    stack<char> s;
    
    for (int i=0; i<l; i++) {
        if (expr[i]=='}' && !s.empty()) {
            if (s.top()=='{') s.pop();
            else s.push(expr[i]);
        }
        else s.push(expr[i]);
    }
    
    int red_len = s.size();
    int n = 0;
    while (!s.empty() && s.top() == '{') {
        s.pop();
        n++;
    }
    return (red_len/2 + n%2);
}
int main() { 
	
	fast_io;
	string s;
	cin >> s;
	cout << countRev(s) << endl;
} 

