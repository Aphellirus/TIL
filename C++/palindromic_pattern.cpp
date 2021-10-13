#include <iostream>
using namespace std;

// Main Program
int main() {
	int n;

	// Taking Input
	cout<<"Enter a Number : ";
	cin>>n;
	cout<<endl;

	//Outer loop for no. of rows
	for(int i = 1; i <= n; i++) {
		// For spaces
		for (int k = (n - i); k > 0; k--) {
			cout<<"  ";
		}
		// First half of the palindrome
		for (int j = i; j >= 2; j--) {
			cout<<j<<" ";
		}
		//Second Half of the Palindrome
		for (int j = 1; j <= i; j++) {
			cout<<j<<" ";
		}
		cout<<endl;
	}
}
