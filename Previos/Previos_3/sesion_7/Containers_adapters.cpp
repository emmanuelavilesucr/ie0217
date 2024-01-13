#include <iostream>
#include <stack>
using namespace std;


int main() {
    
    // create a stack of ints
    stack<int> numbers;

    // push into stack.
    numbers.push(1);
    numbers.push(100);
    numbers.push(10);
 

    cout << "Numbers are: ";

    // we can access the element by getting the top and popping
    // until the stack is empty
    while(!numbers.empty()) {
        // print top element.
        cout << numbers.top() << ", ";

        // pop top element from stack.
        numbers.pop();
    }
    return 0;
}