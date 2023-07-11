#include <iostream>
#include <cstdlib>

int main(int argc, char* argv[])
{
    if (argc != 2)
    {
        std::cout << "Usage: " << argv[0] << " <number of terms>\n";
        return 1;
    }

    int n = std::atoi(argv[1]);

    if (n <= 0)
    {
        std::cout << "Invalid input. Number of terms in the Fibonacci series should be a positive integer.\n";
        return 1;
    }

    unsigned long long fib[n];

    fib[0] = 0; // First Fibonacci term
    fib[1] = 1; // Second Fibonacci term

    // Generate Fibonacci series
    for (int i = 2; i < n; ++i)
    {
        fib[i] = fib[i - 1] + fib[i - 2];
    }

    // Print the Fibonacci series
    for (int i = 0; i < n; ++i)
    {
        std::cout << fib[i] << " ";
    }

    return 0;
}

