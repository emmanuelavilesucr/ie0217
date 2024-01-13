#include <iostream>
#include <vector>
using namespace std;


int main() {

    // Initialize a vector of int type.
    vector<int> numbers = {1, 100, 10, 70, 100};

    // Print the vector.
    cout << "Numbers are: ";
    for(auto &num: numbers) {
        cout << num << ", ";
    }

    return 0;
}
