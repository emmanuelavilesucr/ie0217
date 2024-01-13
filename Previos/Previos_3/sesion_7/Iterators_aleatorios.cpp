#include <iostream>
#include <vector>
using namespace std;


int main() {

    // create a vector
    vector<int> vec{1, 2, 3, 4};

    // create iterators to point to the first and the last elements
    vector<int>::iterator itr_first = vec.begin();
    vector<int>::iterator itr_last = vec.end() - 1;

    // display the vector elements
    cout << "Firt Element: " << *itr_first << endl;
    cout << "Second Element: " << itr_first[1] << endl;

    cout << "Second Last Element: " << *(itr_last - 1) << endl;
    cout << "Last Element: " << *(itr_last) << endl;
    
    return 0;


}