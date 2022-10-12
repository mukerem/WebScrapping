# Time: Jun/28/2022 16:14
# Title: A - Dima and Continuous Line
# Submission ID: 162048206
# Language: Python


x = []
n = int(input())
y = [int(i) for i in input().split()]
for i in range(n-1):
    a,b=  min(y[i], y[i+1]), max(y[i], y[i+1])
    x.append((a, b))
#print(x)
def dima():
    for i in range(n-1):
        for j in range(i+1, n-1):
            a,b = x[i]
            c,d = x[j]
            if a<c<b and b<d or c<a and a<d<b:
                #print(a,b,c,d)
                return 'yes'
    return 'no'
print(dima())
                
        
