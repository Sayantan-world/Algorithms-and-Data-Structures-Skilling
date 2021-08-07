#include <bits/stdc++.h>
using namespace std;

#define fast_io ios_base::sync_with_stdio(false), cin.tie(NULL)
#define ign cin.ignore(numeric_limits<streamsize>::max(),'\n')
typedef vector<int> VI;

int main() {
	
	// Input 
	fast_io;
	int n;
	cin >> n;
    VI v(n);
    for(auto &i: v) cin >> i;
    
    // Get max 2 numbers from the vector
    
    // Initialize 1st, 2nd largest
    int max_1, max_2;
    (v[0] > v[1]) ? (max_1 = v[0], max_2 = v[1]) : (max_2 = v[0], max_1 = v[1]);
    
    // Iterate to find max_1 and max_2
    for(int i = 2; i < n; i++){
		if(v[i] > max_1){
			max_2 = max_1;
			max_1 = v[i];
		}
		else if (v[i] > max_2 && v[i] != max_1) max_2 = v[i];
	}
	cout << max_1 + max_2 << endl;
} 

