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

class AdjListNode {
	
    int v;
    int weight;
public:
    AdjListNode(int _v, int _w)  { v = _v;  weight = _w;}
    int getV()       {  return v;  }
    int getWeight()  {  return weight; }
};
 

class Graph {
	
    int V;
    list<AdjListNode> *adj;
    void topologicalSortUtil(int v, bool visited[], stack<int> &Stack);
public:
    Graph(int V);
    void addEdge(int u, int v, int weight);
    void shortestPath(int s, int k);
};
 
Graph::Graph(int v) {
	
    this->V = v;
    adj = new list<AdjListNode>[V];
}
 
void Graph::addEdge(int u, int v, int weight) {
	
    AdjListNode node(v, weight);
    adj[u].push_back(node);
}
 
void Graph::topologicalSortUtil(int v, bool visited[], stack<int> &Stack) {

    visited[v] = true;
    list<AdjListNode>::iterator i;
    for (i = adj[v].begin(); i != adj[v].end(); ++i) {
        AdjListNode node = *i;
        if (!visited[node.getV()])
            topologicalSortUtil(node.getV(), visited, Stack);
    }
    Stack.push(v);
}

void Graph::shortestPath(int s, int k) {
	
    stack<int> Stack;
    int dist[V];
    bool *visited = new bool[V];
    for (int i = 0; i < V; i++)
        visited[i] = false;
    for (int i = 0; i < V; i++)
        if (visited[i] == false)
            topologicalSortUtil(i, visited, Stack);
    for (int i = 0; i < V; i++)
        dist[i] = INF;
    dist[s] = 0;
    while (Stack.empty() == false) {
        int u = Stack.top();
        Stack.pop();
        list<AdjListNode>::iterator i;
        if (dist[u] != INF) {
          for (i = adj[u].begin(); i != adj[u].end(); ++i)
             if (dist[i->getV()] > dist[u] + i->getWeight())
                dist[i->getV()] = dist[u] + i->getWeight();
        }
    }
    for (int i = 0; i < V; i++)
        if(i == k) (dist[i] == INF)? cout << "-1" << endl: cout << dist[i] << endl;
}

int main() {
	
	fast_io;
	ll n, k;
	cin >> n;
	int mat[n][n];
	for(int i = 0; i < n; i++){
		for(int j = 0; j< n; j++){
			int temp;
			cin >> temp;
			mat[i][j] = temp;
		}
	}
	Graph g(n);
	for(int i = 0; i < n; i++){
		for(int j = 0; j< n; j++){
			if(mat[i][j] != 0) g.addEdge(i, j, mat[i][j]);
		}
	}
	cin >> k;
    g.shortestPath(0, k);
}

