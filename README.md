# Coin Change Algorithms

## Greedy Algorithm

The greedy algorithm iteratively selects the largest possible denomination until the amount is reached. It is efficient and runs in \(O(n)\) time complexity, where \(n\) is the number of coin types. This method is quick and simple but may not always yield the optimal solution, depending on the coin denominations.

## Dynamic Programming Algorithm

The dynamic programming approach ensures the minimum number of coins by exploring all combinations. It has a time complexity of \(O(n \times m)\), where \(n\) is the number of coin types and \(m\) is the amount. This method guarantees the optimal solution by finding the minimum number of coins needed.

## Performance Comparison

- **Greedy Algorithm:** Fast and easy to implement, suitable for coin sets where it guarantees an optimal solution.
- **Dynamic Programming:** More computationally intensive but always finds the optimal solution. Ideal for arbitrary coin sets.

### Execution Times

- **Greedy Algorithm Time:** The greedy algorithm was timed using `timeit` and found to be very efficient for small to moderately large amounts.
- **Dynamic Programming Time:** The dynamic programming algorithm, while more complex, ensures the minimal number of coins, making it more reliable for arbitrary coin sets.

### Conclusion

In scenarios with large amounts or complex coin sets, the dynamic programming approach is preferable due to its guarantee of finding the minimum number of coins. The greedy algorithm, however, is much faster and simpler to implement when it is known that it will yield an optimal solution.
