"""
Given 3 numbers {1, 3, 5}, find the total number of ways we can form a number 'N' using the sum of the given 3 numbers.
(allowing repetitions and different arrangements).

Example 1:

Input: 
N = 6
arr = {1,3,5}
Output: 8
Explanation:

Total number of ways to form 6 is: 8
1+1+1+1+1+1
1+1+1+3
1+1+3+1
1+3+1+1
3+1+1+1
3+3
1+5
5+1

DP Approach:

1) Adding 1 to all possible combinations of state (n = 6) 
Eg : [ (1+1+1+1+1+1) + 1] 
[ (1+1+1+3) + 1] 
[ (1+1+3+1) + 1] 
[ (1+3+1+1) + 1] 
[ (3+1+1+1) + 1] 
[ (3+3) + 1] 
[ (1+5) + 1] 
[ (5+1) + 1] 

2) Adding 3 to all possible combinations of state (n = 4);
Eg : [(1+1+1+1) + 3] 
[(1+3) + 3] 
[(3+1) + 3] 

3) Adding 5 to all possible combinations of state(n = 2) 
Eg : [ (1+1) + 5]

Therefore, we can say that result for 
state(7) = state (6) + state (4) + state (2) 
or 
state(7) = state (7-1) + state (7-3) + state (7-5)
In general, 
state(n) = state(n-1) + state(n-3) + state(n-5)

"""


class SumOfArray:

    # Recursion:[Top down]
    class Recursion:
        def arraySum(self, N):
            if(N < 0):
                return 0
            if(N == 0):
                return 1
            return self.arraySum(N-1)+self.arraySum(N-3)+self.arraySum(N-5)

    # Memoization:[Bottom Up]
    class Memoization:
        def arraySum(self, N):
            lookup = {}
            if(N < 0):
                return 0
            if(N == 0):
                return 1
            if(N not in lookup):
                lookup[N] = self.arraySum(
                    N-1)+self.arraySum(N-3)+self.arraySum(N-5)

            return lookup[N]


sumObject = SumOfArray()
recursionObject = sumObject.Recursion()
memoizationObject = sumObject.Memoization()
print("Using Recursion : ", recursionObject.arraySum(6))
print("Using Memoization : ", memoizationObject.arraySum(6))
