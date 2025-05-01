# CMPS 2200 Assignment 3
## Answers

**Name:** Mary Ella Scroggie


Place all written answers from `assignment-03.md` here for easier grading.

- 1a take the largest coin such that 2^k ≤ N, then subtract that from N, then repeat for the largest value of 2^j <= N-2^k

- 1b, Yes, the problem can be divided into sub problems that are all solved by the greedy algorithm and the result is optimal
- 1c the work and span are both O(n)= log(n)
- 2a if the coins are 1, 4, 5 and N is 13, a greedy algorithm would choose 5,5,1,1,1, when the optimal solution is 5,4,4

- 2b Optimal substructure property is when a problem can be divided into sub problems, and those optimal solutions are used to find the optimal solution of the bigger problem.
to solve the above problem, once you choose 5 you can solve the sub problem of the optimal way to get 8

- 2c  
-           N
-       /  /  \  \ *number of types of coins
-     c1  c2  c3  cn 
-     / / \ \
-    c11c12c13c1n
  ...
  when an end is reached, add it to the dictionary
  compute for the other combos, referencing the dictionary
  compute coins(N)
  dictionary()
  while sum > 0:
      for coin in coins:
          sum = N - coin
          route.append(coin)
          compute coins(sum)
- the work is O(N) = N * k and the span is O(N) = N * log k
