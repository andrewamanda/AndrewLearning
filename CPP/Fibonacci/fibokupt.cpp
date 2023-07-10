#include <iostream>

int main() {
    int n = 100; // Number of terms to generate
    unsigned long long int fib[n];

    fib[0] = 0; // First Fibonacci term
    fib[1] = 1; // Second Fibonacci term

    // Generate Fibonacci series
    for (int i = 2; i < n; ++i) {
        fib[i] = fib[i - 1] + fib[i - 2];
    }
  
    // Print the Fibonacci series
    for (int i = 0; i < n; ++i) {
        std::cout << fib[i] << " ";
    }
  
    return 0;
}

