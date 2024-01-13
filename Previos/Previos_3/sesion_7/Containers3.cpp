#include <iostream>
#include <unordered_set>
using namespace std;


int main() {

    // Initialize a unordered_set of int type.
    unordered_set<int> numbers = {1, 100, 10, 70, 100};

    // Print the set.
    cout << "Numbers are: ";
    for(auto &num: numbers) {
        cout << num << ", ";
    }

    return 0;
}
