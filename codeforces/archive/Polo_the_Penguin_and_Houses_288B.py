# Time: Jul/16/2022 14:17
# Title: B - Polo the Penguin and Houses
# Submission ID: 164435771
# Language: Python


def number_of_ways(n: int, k: int) -> int:
    mod = int(1e9) + 7
    return (pow(k,k-1,mod)*pow(n-k,n-k,mod))%mod
n,k = [int(i) for i in input().split()]
print(number_of_ways(n, k))
