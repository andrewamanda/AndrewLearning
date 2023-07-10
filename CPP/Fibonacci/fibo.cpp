#include <iostream>
#include <vector>

int main() {
    std::vector<long long> fibonacci(50);
    fibonacci[0] = 0;
    fibonacci[1] = 1;
    
    std::cout << "The first 50 terms of the Fibonacci sequence are: \n";
    
    // Compute the terms of the Fibonacci sequence
    for (int i = 2; i < 50; ++i) {
        fibonacci[i] = fibonacci[i-1] + fibonacci[i-2];
    }
    
    // Output the terms of the Fibonacci sequence
    for (int i = 0; i < 50; ++i) {
        std::cout << "Fibonacci[" << i << "] = " << fibonacci[i] << '\n';
    }
    
    return 0;
}

