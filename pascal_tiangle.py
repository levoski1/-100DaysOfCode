from math import factorial

# Pascal's Triangle Generator

'''
Steps to Generate Pascal's Triangle:

1. **Understanding the Triangle**:
    - The triangle starts with a single 1 at the top (0th row).
    - Each subsequent row starts and ends with 1.
    - Each number inside the triangle is the sum of the two numbers directly above it.
    - Mathematically, each element in the row can be represented using the binomial coefficient formula:

      nCr =   n!
             ------
             r! (n-r)!

    - Where `n` is the row number, and `r` is the position within the row.

2. **Example Breakdown**:

       Row 0:           1                   ->                  0C0
       Row 1:         1   1                 ->              1C0     1C1
       Row 2:       1   2   1               ->           2C0    2C1     2C2
       Row 3:     1   3   3   1             ->       3C0    3C1     3C2     3C3
       Row 4:   1   4   6   4   1           ->   4C0     4C1    4C2     4C3     4C4

3. **Steps in Code**:
    - Get the number of rows from the user (e.g., `row = 5`).
    - Loop through the range of rows (0 to `row-1`).
    - For each row, calculate the binomial coefficient for each position and print the result.

'''

def pascal_triangle(row):
    for n in range(row):
        # Print spaces for alignment (optional, to center-align the triangle)
        for space in range(1, row - n):
            print(end=' ')
            

        for r in range(n + 1):
            ncr = factorial(n) // (factorial(r) * factorial(n - r))
            print(ncr, end=' ')
        
        # Move to the next line after printing all positions in the row
        print('')

