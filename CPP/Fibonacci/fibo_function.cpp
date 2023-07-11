#include <iostream>
#include <cstdlib>

// Function to generate Fibonacci series
void generateFibonacci(int n)
{
    unsigned long long fib[n];

    fib[0] = 0; // First Fibonacci term
    fib[1] = 1; // Second Fibonacci term

    for (int i = 2; i < n; ++i)
    {
        fib[i] = fib[i - 1] + fib[i - 2];
    }

    for (int i = 0; i < n; ++i)
    {
        std::cout << fib[i] << " ";
    }
}

int main(int argc, char* argv[])
{
    if (argc != 2)
    {
        std::cout << "Usage: " << argv[0] << " \n";
        return 1;
    }

    int n = std::atoi(argv[1]);

    if (n <= 0)
    {
        std::cout << "Invalid input. Number of terms in the Fibonacci series should be a positive integer.\n";
        return 1;
    }

    generateFibonacci(n);

    return 0;
}

