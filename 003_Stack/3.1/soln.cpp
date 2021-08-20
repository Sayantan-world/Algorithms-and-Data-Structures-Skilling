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

void s_push(stack<int>& mystack, ll value){
	
	if((int)mystack.size() == 10) cout << "stack is full" << endl;
	else{
		mystack.push(value);
	}
}

void s_pop(stack<int>& mystack){
	if((int)mystack.size() == 0) cout << "stack is empty" << endl;
	else {
		mystack.pop();
	}
}

int main() { 
	
	fast_io;
	ll n;
	cin >> n;
	stack<int> mystack;
	
	for(ll i = 0; i < n;){
		ll task;
		cin >> task;
		//~cout << task << " ";
		i++;
		if(task == 1){
			ll value;
			cin >> value;
			//~cout << value << " ";
			i++;
			s_push(mystack, value);
		}
		else if(task == 2){
			s_pop(mystack);
		}
		else{
			if((int)mystack.size() == 0) cout << "stack is empty" << endl;
			else{
				while (!mystack.empty()) {
					cout << mystack.top() << " ";
					mystack.pop();
				}
				cout << endl;
			}
		}
	}
	
} 

