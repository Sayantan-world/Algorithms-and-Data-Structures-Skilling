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
	
    int data;
    BST *left, *right;
    
public:
    BST();
    BST(int);
    BST* Insert(BST*, int);
    BST* kthSmallest(BST*, int&);
    void getKsmallest(BST*, int);
    void Inorder(BST*);
};
 
// Default Constructor
BST :: BST() : data(0), left(NULL), right(NULL){}
 
// Parameterized Constructor
BST ::BST(int value) {
    data = value;
    left = right = NULL;
}
 
// Insert function 
BST* BST ::Insert(BST* root, int value) {
    if (!root) return new BST(value);
    // Insert data.
    if (value > root->data) root->right = Insert(root->right, value);
    else root->left = Insert(root->left, value);
    return root;
}

void BST ::Inorder(BST* root) {
    if (!root) {
        return;
    }
    Inorder(root->left);
    cout << root->data << " ";
    Inorder(root->right);
}

BST* BST::kthSmallest(BST* root, int& k) {

    if (root == NULL) return NULL;
    BST* l = kthSmallest(root->left, k);
    if (l != NULL) return l;
    k--;
    if (k == 0) return root;
    return kthSmallest(root->right, k);
}

void BST::getKsmallest(BST* root, int k) {
	
    BST* res = kthSmallest(root, k);
    if (res == NULL) cout << -1 << endl; 
    else cout << res->data << endl;
}


int main() {
	
	fast_io;
	ll n;
	cin >> n;
    int ip[n];
	for(auto &i: ip) cin >> i;
    BST b, *root = NULL;
    int k;
    cin >> k;
	if(n > 0){
		root = b.Insert(root, ip[0]);
		for(int i = 1; i < n; i++){
			b.Insert(root, ip[i]);
		}
		b.getKsmallest(root, k);
	}
    return 0;
}

