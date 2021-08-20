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


int maxLen(string str) {
	
    int n = str.length();
    stack<int> stk;
    stk.push(-1);
    int answer = 0;
    
    for (int i = 0; i < n; i++) {
        if (str[i] == '(') stk.push(i);
        else {
            if (!stk.empty()) stk.pop();
            if (!stk.empty()) answer = max(answer, i - stk.top());
            else stk.push(i);
        }
    }
 
    return answer;
}

int main() { 
	
	fast_io;
	string s;
	cin >> s;
	cout << maxLen(s) << endl;
} 

