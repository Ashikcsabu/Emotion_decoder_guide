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