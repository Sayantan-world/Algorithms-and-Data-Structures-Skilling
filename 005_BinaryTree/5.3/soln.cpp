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

class node {
    public:
    char data;
    node* left;
    node* right;
};

int search(char arr[], int strt, int end, char value);
node* newNode(char data);

node* buildTree(char in[], char pre[], int inStrt, int inEnd) {
	
    static int preIndex = 0;
    if (inStrt > inEnd) return NULL;
    node* tNode = newNode(pre[preIndex++]);
    if (inStrt == inEnd) return tNode;
    int inIndex = search(in, inStrt, inEnd, tNode->data);
    tNode->left = buildTree(in, pre, inStrt, inIndex - 1);
    tNode->right = buildTree(in, pre, inIndex + 1, inEnd);
    return tNode;
}

int search(char arr[], int strt, int end, char value) {
    int i;
    for (i = strt; i <= end; i++) {
        if (arr[i] == value)
            return i;
    }
    return i;
}

node* newNode(char data) {
    node* Node = new node();
    Node->data = data;
    Node->left = NULL;
    Node->right = NULL;
    return (Node);
}

void print_tree(node* node) {
	
    if (node == NULL) return;
    print_tree(node->left);
    cout<<node->data<<" ";
    print_tree(node->right);
}

int main() {
	
	fast_io;
	ll n;
	cin >> n;
    char in[n];
    char pre[n];
	for(auto &i: in) cin >> i;
    for(auto &i: pre) cin >> i;
    node* root = buildTree(in, pre, 0, n - 1);
    print_tree(root);
	cout << endl;
 
    return 0;
}

