#include <iostream>

int main() {
    int n = 10; // Number of terms to generate
    unsigned long long int fib[n];

    fib[0] = 0; // First Fibonacci term
    fib[1] = 1; // Second Fibonacci term

    // Generate Fibonacci series
    for (int i = 2; i < n; ++i) {
        fib[i] = fib[i - 1] + fib[i - 2];
    }

    // Print the Fibonacci series
    for (int i = 0; i < n; ++i) {
        for (unsigned long long int j = 0; j < fib[i]; ++j) {
            std::cout << "*";
        }
        std::cout << "\n";
    }

    return 0;
}

