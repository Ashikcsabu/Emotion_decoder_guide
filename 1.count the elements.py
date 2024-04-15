class Solution:
    def countElements(self, a, b, n, query, q):
        max_val = max(max(a), max(b)) + 1  # Find the maximum value in a and b
        hash_table = [0] * max_val  # Initialize hash table

        # Populate hash table with counts of elements in array b
        for num in b:
            hash_table[num] += 1

        # Compute cumulative counts in hash table
        for i in range(1, max_val):
            hash_table[i] += hash_table[i - 1]

        ans = []  # List to store the answers for each query
        for i in range(q):
            count = hash_table[a[query[i]]]  # Count elements in b less than or equal to a[query[i]]
            ans.append(count)
        return ans


#{
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    q = int(input())
    query = []
    ob = Solution()
    for i in range(q):
        query.append(int(input()))
    ans = ob.countElements(a, b, n, query, q)
    for i in range(q):
        print(ans[i])

# } Driver Code Ends



#normal logic of the program :
"""Given two arrays a and b both of size n. Given q queries in an array query each having a positive integer x denoting an index of the array a. For each query, your task is to find all the elements less than or equal to a[x] in the array b.

Example 1:

Input:
n = 3
a[] = {4,1,2}
b[] = {1,7,3}
q = 2
query[] = {0,1}
Output : 
2
1
Explanation: 
For 1st query, the given index is 0, a[0] = 4. There are 2 elements(1 and 3) which are less than or equal to 4.
For 2nd query, the given index is 1, a[1] = 1. There exists only 1 element(1) which is less than or equal to 1.

Python code:

n = 3#number of elemts in a and b
a= [4,1,2]
b = [1,7,3]
q = 2 #query parameter size
query = [0,1]
for i in query:
    ct=0
    for j in b:
        if j<=a[i]:
            ct+=1
    print(ct)
"""


