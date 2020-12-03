## what is big O
> Big O notation is special notation that tells you how fast an algorithm is.
> Estimate of __how well a computer algorithm scales__ as the amount of data involved increases e.g how well it runs for a 5 element array vs a 5000 element array.
> Big O establishes a worst case run time / upper bound
> Algo speed is not measured in seconds, but in growth of number of operations

## Rules
> example: 4n^2 + 50n + 84
1. Always worst Case
2. Drop the constants, remove 84, 50 and 4
3. Different inputs should have different variables. O(a+b). A and B arrays nested would be O(a*b)
4. Drop non-dominant terms, remove n^2. Finally O(n^2) is the run time

# Important Points
* O(1) Constant - no loops
* O(log N) Logarithmic - usually searching algortihms have log n if they are sorted (binary search)
* O(n) Linear - for loops, while loops through n items e.g. Simple Search
* O(n log(n)) Log Linear - usually sorting algos e.g. quick sort
* O(2^n) Exponential - recusrive algos that solve problem of size N
* O(n!) Factorial - loop for every element in array e.g. Travelling SalesPerson

# Logs are flip of exponents
Binary Search has log(n) run time. e.g.
list of 8 elements you have to check 3 times, How? log 8 ==3, because 2^3 =8
list of 1024 elements, you have to check 10 times, How? log 1024 = 10, because 2^10 = 1024

## Asymptotic Analysis




