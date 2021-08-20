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

struct Edge {
    int src, dest;
};
 
class Graph {
	
public:
    vector<vector<int>> adjList;
    Graph(vector<Edge> const &edges, int N) {
        adjList.resize(N);
        for (auto &edge: edges) {
            adjList[edge.src].push_back(edge.dest);
        }
    }
};

bool isConnected(Graph const graph, int src, int dest, vector<bool> discovered) {
    queue<int> q;
    discovered[src] = true;
    q.push(src);
    while (!q.empty()) {
        int v = q.front();
        q.pop();
        if (v == dest) {
            return true;
        }
        for (int u: graph.adjList[v]) {
            if (!discovered[u]) {
                discovered[u] = true;
                q.push(u);
            }
        }
    }
 
    return false;
}

int main() {
	
	fast_io;
	ll n;
	cin >> n;
	int mat[n][n];
	for(int i = 0; i < n; i++){
		for(int j = 0; j< n; j++){
			int temp;
			cin >> temp;
			mat[i][j] = temp;
		}
	}
	vector<Edge> edges = {};
	vector<bool> discovered(n);
	for(int i = 0; i < n; i++){
		for(int j = 0; j< n; j++){
			if(mat[i][j] != 0) 
				edges.pb({i,j});
		}
	}
	Graph graph(edges, n);
	int k;
	cin >> k;
    int src = k;
    int ans = 0;
    for(int i = 0; i < n; i++){
		if(i!=src){
			if (isConnected(graph, src, i, discovered)) {
				ans++;
			}
		}
	}
	cout << ans << endl;
}

