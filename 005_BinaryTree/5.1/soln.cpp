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

struct Node {
    int key;
    struct Node *left, *right;
};
 
Node *newNode(int key) {
    Node *temp = new Node;
    temp->key  = key;
    temp->left  = temp->right = NULL;
    return (temp);
}

void createNode(VL parent, int i, Node *created[], Node **root) {
	
    if (created[i] != NULL)
        return;

    created[i] = newNode(i);

    if (parent[i] == -1) {
        *root = created[i];
        return;
    }

    if (created[parent[i]] == NULL) createNode(parent, parent[i], created, root);
 
    Node *p = created[parent[i]];

    if (p->left == NULL) p->left = created[i];
    else p->right = created[i];
}

Node *createTree(VL parent, int n) {
    Node *created[n];
    for (int i=0; i<n; i++) created[i] = NULL;
 
    Node *root = NULL;
    for (int i=0; i<n; i++) createNode(parent, i, created, &root);
 
    return root;
}

void inorder(Node *root) {
    if (root != NULL) {
        inorder(root->left);
        cout << root->key << " ";
        inorder(root->right);
    }
}
 
int main() {
	
	fast_io;
	ll n;
	cin >> n;
    VL parent(n);
    for(auto &i: parent) cin >> i;
    Node *root = createTree(parent, n);
    inorder(root);
    cout << endl;
}

