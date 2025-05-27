from notebooks.general_utils import *

def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def find_min_rows_sum_to_zero(P):
    k, n_k = P.shape
    
    # Try all possible combinations of rows
    for i in range(1, k + 1):
        for combination in combinations(range(k), i):
            # Vector sum
            ans = [0] *(n_k)
            for row in combination:
                for id in range(0,n_k):
                    ans[id] ^= P[row, id]

            # Check if sum is zero vector
            if np.all(ans == np.zeros(n_k)):
                return combination
    return []