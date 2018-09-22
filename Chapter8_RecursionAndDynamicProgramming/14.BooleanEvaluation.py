"""Boolean Evaluation (Boolean Parenthesization)

Given a boolean expression consisting of the symbols 0 (false), 1 (true), &
(AND), | (OR), and ^ (XOR), and a desired boolean result value result, implement a function to
count the number of ways of parenthesizing the expression such that it evaluates to result.

EXAMPLE
countEval("1^0|0|1", false) -> 2
countEval("0&0&0&1^1|0, true) -> 10

Hints: 
#148
Can we just try all possibilities? What would this look like?
#168
We can think about each possibility as each place where we can put parentheses. This
means around each operator, such that the expression is split at the operator. What is
the base case?
#197
The base case is when we have a single value, 1 or O.
#305
If your code looks really lengthy, with a lot of if's (for each possible operator, "target"
boolean result, and left/right side), think about the relationship between the different
parts. Try to simplify your code. It should not need a ton of complicated if-statements.
For example, consider expressions of the form <LEFT>OR<RIGHT> versus
<LEFT>AND<RIGHT>. Both may need to know the number of ways that the <LEFT>
evaluates to true. See what code you can reuse.
#327
Look at your recursion. Do you have repeated calls anywhere? Can you memoize it?
"""

'''Method 1

This is recursive method. 
We can see this problem as function(expression, result). 
We go through all the operators in the expression, 
so the function(expression, result) splits into two functions; function(expression left, result),
function(expression right, result) and continues to split it until the length of expression is 1.
'''

def count_boolean_evaluation(expression, result):
    if len(expression) == 1:
        return 1 if (expression == "1" and result) or (expression == "0" and not result) else 0
    count = 0
    for i in range(1, len(expression), 2):
        left = expression[:i] 
        right = expression[i+1:]
        if expression[i] == "|":
            if result:
                count += count_boolean_evaluation(left, True) * count_boolean_evaluation(right, True)
                count += count_boolean_evaluation(left, True) * count_boolean_evaluation(right, False)
                count += count_boolean_evaluation(left, False) * count_boolean_evaluation(right, True)
            else:
                count += count_boolean_evaluation(left, False) * count_boolean_evaluation(right, False)
        elif expression[i] == "&":
            if result:
                count += count_boolean_evaluation(left, True) * count_boolean_evaluation(right, True)
            else:
                count += count_boolean_evaluation(left, True) * count_boolean_evaluation(right, False)
                count += count_boolean_evaluation(left, False) * count_boolean_evaluation(right, True)
                count += count_boolean_evaluation(left, False) * count_boolean_evaluation(right, False)
        elif expression[i] == "^":
            if result:
                count += count_boolean_evaluation(left, True) * count_boolean_evaluation(right, False)
                count += count_boolean_evaluation(left, False) * count_boolean_evaluation(right, True)
            else:
                count += count_boolean_evaluation(left, True) * count_boolean_evaluation(right, True)
                count += count_boolean_evaluation(left, False) * count_boolean_evaluation(right, False)
    return count

'''Method 2

The recursion solution has a high time complexity that we have calculated multiple times. 
We can use 3 dimensions array to store all the values. 
DP[expression length][expression length][2 – True or False]
It initializes table using expression.

For example: 1^0|0|1
initial it would DP[0][0][1] = 1; DP[2][2][0] = 1; DP[4][4][0] = 1; DP[6][6][1] = 1;
then we start to gap 2 values
DP[0][2][0 or 1]; DP[2][4][0 or 1]; DP[4][6][0 or 1] from all the previous values we know
then gap 4 values
DP[0][4][0 or 1]; DP[2][6][0 or 1];
then  gap 6 values
DP[0][6][0 or 1] which is what we want.
'''
def count_boolean_evaluation_by_dp(expression, result):
    dp = [[[0, 0] for _ in range(len(expression))] for _ in range(len(expression))]
    for i in range(0, len(dp), 2):
        for j in range(0, len(dp[0]), 2):
            if i == j:
                if expression[i] == "1":
                    dp[i][j][1] = 1
                else:    
                    dp[i][j][0] = 1    
    for length in range(3, len(expression)+1, 2):        
        for start in range(0, len(expression)+1-length, 2):            
            for k in range(start+1, start+length, 2):                
                end = start + length - 1                
                if expression[k] == "|":
                    dp[start][end][1] += dp[start][k-1][1] * dp[k+1][end][1] + \
                                        dp[start][k-1][0] * dp[k+1][end][1] + \
                                        dp[start][k-1][1] * dp[k+1][end][0]
                    dp[start][end][0] += dp[start][k-1][0] * dp[k+1][end][0]
                elif expression[k] == "&":
                    dp[start][end][1] += dp[start][k-1][1] * dp[k+1][end][1]
                    dp[start][end][0] += dp[start][k-1][0] * dp[k+1][end][0] + \
                                        dp[start][k-1][0] * dp[k+1][end][1] + \
                                        dp[start][k-1][1] * dp[k+1][end][0]
                elif expression[k] == "^":
                    dp[start][end][1] += dp[start][k-1][0] * dp[k+1][end][1] + \
                                        dp[start][k-1][1] * dp[k+1][end][0]
                    dp[start][end][0] += dp[start][k-1][0] * dp[k+1][end][0] + \
                                        dp[start][k-1][1] * dp[k+1][end][1]                
    return dp[0][len(expression)-1][1 if result else 0]


import unittest

class Test(unittest.TestCase):
    def test_count_boolean_evaluation(self):
        self.assertEqual(count_boolean_evaluation("1^0|0|1", False), 2)        
        self.assertEqual(count_boolean_evaluation("0&0&0&1^1|0", True), 10)

    def test_count_boolean_evaluation_by_dp(self):
        self.assertEqual(count_boolean_evaluation_by_dp("1^0|0|1", False), 2)        
        self.assertEqual(count_boolean_evaluation_by_dp("0&0&0&1^1|0", True), 10)

if __name__ == "__main__":
    unittest.main()