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


void q_push_f(deque<int>& mydeque, ll value){
	
	if((int)mydeque.size() == 10) cout << "deque is full" << endl;
	else{
		mydeque.push_front(value);
	}
}
void q_push_r(deque<int>& mydeque, ll value){
	
	if((int)mydeque.size() == 10) cout << "deque is full" << endl;
	else{
		mydeque.push_back(value);
	}
}

void q_pop_f(deque<int>& mydeque){
	if((int)mydeque.size() != 0) mydeque.pop_front();
}

void q_pop_r(deque<int>& mydeque){
	if((int)mydeque.size() != 0) mydeque.pop_back();
}

int main() { 
	
	fast_io;
	ll n;
	cin >> n;
	deque<int> mydeque;
	
	VL values(n);
	VL task(n);
	
	for(auto &i: values) cin >> i;
	for(auto &i: task) cin >> i;
	
	for(int i = 0; i < n ; i++){
		if(task[i] == 1){
			q_push_f(mydeque, values[i]);
		}		
		else if(task[i] == 2){
			q_push_r(mydeque, values[i]);
		}
		else if(task[i] == 3){
			q_pop_f(mydeque);
		}
		else {
			q_pop_r(mydeque);
		}
	}
	
	while (!mydeque.empty()) {
		cout << mydeque.front() << " ";
		mydeque.pop_front();
	}
	cout << endl;
} 

