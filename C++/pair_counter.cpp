#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Returns the number of pairs in a given vector
int pair_count(vector<int> ar)
{
    vector<int> record = vector<int>();
    int pairs {};
    
    for (int item : ar)
    {
        if (find(record.begin(), record.end(), item) != record.end()) // Check for pre-existing elements
		 {
		  	pairs++;  
		 }
		 else // Add to storage vector if none is found
		 {
		  	record.push_back(item);
		 }
    }
    
    return pairs;
}

int main() {

	vector<int> input = {1, 2, 1, 3, 2, 5};
	
	int result = pair_count(input);
	
	cout << result << "\n";

	return 0;
}
