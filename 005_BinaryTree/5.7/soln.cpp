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
    int data;
    Node *left, *right;
};
 
Node* newNode(int data);
 
int search(int arr[], int strt, int end, int value);

Node* buildUtil(int in[], int post[], int inStrt, int inEnd, int* pIndex) {

    if (inStrt > inEnd) return NULL;
    Node* node = newNode(post[*pIndex]);
    (*pIndex)--;
    if (inStrt == inEnd) return node;
    int iIndex = search(in, inStrt, inEnd, node->data);
    node->right = buildUtil(in, post, iIndex + 1, inEnd, pIndex);
    node->left = buildUtil(in, post, inStrt, iIndex - 1, pIndex);
    return node;
}

Node* buildTree(int in[], int post[], int n){
    int pIndex = n - 1;
    return buildUtil(in, post, 0, n - 1, &pIndex);
}

int search(int arr[], int strt, int end, int value) {
    int i;
    for (i = strt; i <= end; i++) {
        if (arr[i] == value)
            break;
    }
    return i;
}

Node* newNode(int data) {
    Node* node = (Node*)malloc(sizeof(Node));
    node->data = data;
    node->left = node->right = NULL;
    return (node);
}

void print_tree(Node* node) {
    if (node == NULL) return;
    cout << node->data << " ";
	print_tree(node->left);
    print_tree(node->right);
}
int main() {
	
	fast_io;
	ll n;
	cin >> n;
    int in[n];
    int post[n];
	for(auto &i: post) cin >> i;
    for(auto &i: in) cin >> i;
    Node* root = buildTree(in, post, n);
    print_tree(root);
	cout << endl;
 
    return 0;
}

