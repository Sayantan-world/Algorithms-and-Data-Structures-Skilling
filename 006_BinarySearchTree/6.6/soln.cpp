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

#include <iostream>
using namespace std;
 
class BST {
	public:
    int data;
    BST *left, *right;
    BST();
    BST(int);
    BST* Insert(BST*, int);
	BST* lca(BST*, int, int);
    void Inorder(BST*);
};
 
// Default Constructor
BST::BST() : data(0), left(NULL), right(NULL){}
 
// Parameterized Constructor
BST::BST(int value) {
    data = value;
    left = right = NULL;
}
 
// Insert function 
BST* BST::Insert(BST* root, int value) {
    if (!root) return new BST(value);
    // Insert data.
    if (value > root->data) root->right = Insert(root->right, value);
    else root->left = Insert(root->left, value);
    return root;
}

BST* BST::lca(BST* root, int n1, int n2) {
    while (root != NULL) {
        if (root->data > n1 && root->data > n2) root = root->left;
        else if (root->data < n1 && root->data < n2) root = root->right;
        else break;
    }
    return root;
}

void BST::Inorder(BST* root) {
    if (!root) {
        return;
    }
    Inorder(root->left);
    cout << root->data << " ";
    Inorder(root->right);
}

int main() {
	
	fast_io;
	ll n;
	cin >> n;
    int ip[n];
	for(auto &i: ip) cin >> i;
    BST b, *root = NULL;
    int n1, n2;
    cin >> n1 >> n2;
	if(n > 0){
		root = b.Insert(root, ip[0]);
		for(int i = 1; i < n; i++){
			b.Insert(root, ip[i]);
		}
		BST *temp = b.lca(root, n1, n2);
		cout << temp->data << endl;
			
	}
    return 0;
}

