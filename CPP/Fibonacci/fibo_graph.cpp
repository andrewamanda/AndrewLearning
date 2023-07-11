#include <iostream>
#include <vector>
#include <algorithm>

// Function to draw the Fibonacci spiral using ASCII art
void drawFibonacciSpiral(const std::vector<unsigned long long>& sequence)
{
    // Constants for ASCII representation
    char empty = ' ';
    char filled = '#';

    // Determine the size of the grid based on the maximum Fibonacci number
    unsigned long long maxFib = *std::max_element(sequence.begin(), sequence.end());
    int gridSize = maxFib * 2;

    // Initialize the grid with empty spaces
    std::vector<std::vector<char> > grid(gridSize, std::vector<char>(gridSize, empty));

    // Starting position and initial direction
    int x = gridSize / 2;
    int y = gridSize / 2;
    int dx = 0;
    int dy = -1;

    // Fill the grid with the spiral pattern
    for (unsigned long long fib : sequence)
    {
        for (unsigned long long i = 0; i < fib; i++)
        {
            // Check if coordinates are within the grid boundaries
            if (x >= 0 && x < gridSize && y >= 0 && y < gridSize)
                grid[y][x] = filled;

            // Move to the next position
            x += dx;
            y += dy;
        }

        // Change direction (rotate counterclockwise)
        int temp = dx;
        dx = -dy;
        dy = temp;
    }

    // Print the ASCII representation of the grid
    for (const auto& row : grid)
    {
        for (char cell : row)
            std::cout << cell;
        
        std::cout << std::endl;
    }
}

int main()
{
    int n = 100; // Number of terms to generate
    std::vector<unsigned long long> fib(n);

    fib[0] = 0; // First Fibonacci term
    fib[1] = 1; // Second Fibonacci term

    // Generate Fibonacci series
    for (int i = 2; i < n; ++i)
    {
        fib[i] = fib[i - 1] + fib[i - 2];
    }
  
    // Draw the Fibonacci spiral using ASCII art
    drawFibonacciSpiral(fib);
  
    return 0;
}

