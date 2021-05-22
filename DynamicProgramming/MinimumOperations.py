"""Given a number N. Find the minimum number of operations required to reach N starting from 0. You have 2 operations available:

Double the number
Add one to the number

Example 1:

Input:
N = 8
Output: 4
Explanation: 0 + 1 = 1, 1 + 1 = 2,
2 * 2 = 4, 4 * 2 = 8

Example 2:

Input: 
N = 7
Output: 5
Explanation: 0 + 1 = 1, 1 + 1 = 2,
1 + 2 = 3, 3 * 2 = 6, 6 + 1 = 7

Your Task:
You don't need to read input or print anything. Your task is to complete the function minOperation() which accepts an integer N and return number of minimum operations required to reach N from 0.


Expected Time Complexity: O(LogN)
Expected Auxiliary Space: O(1)


Constraints:
1 <= N <= 106

Correct Answer.Correct Answer
Execution Time:0.02
"""


class Solution:

    def minOperation(self, n):
        op = 2
        if(n == 1):
            return 1
        elif(n == 2):
            return 2
        else:
            while(n != 2):
                if(n % 2 == 0):
                    n /= 2
                    op += 1
                else:
                    n -= 1
                    op += 1
        return op


solution_obj = Solution()
print(solution_obj.minOperation(int(input("Enter a number N: "))))
