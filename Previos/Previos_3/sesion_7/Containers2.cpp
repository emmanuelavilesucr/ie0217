#include <iostream>
#include <set>
using namespace std;


int main() {

    // Initialize a set of int type.
    set<int> numbers = {1, 100, 10, 70, 100};

    // Print the set.
    cout << "Numbers are: ";
    for(auto &num: numbers) {
        cout << num << ", ";
    }

    return 0;
}
