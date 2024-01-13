#include <iostream>
#include <forward_list>
using namespace std;


int main() {

    forward_list<int> nums{1, 2, 3, 4};

    // initialize an iterator to point 
    // to beginning of a forward list
    forward_list<int>::iterator itr = nums.begin();

    while (itr != nums.end()) {
 
        // access iterator value using indirection operator
        int original_value = *itr;

        // assign new value using indirection operator
        *itr = original_value * 2;
        
        // forward the iterator to next position
        itr++;
    }

    // display the contents of nums
    for (int num: nums) {
        cout << num << ", ";
    } 
    return 0;
}