def fib(n,memo):
    global c
    c=c+1
    if n in memo.keys():
        return memo[n]
    if n<0:
        return
    if n==0:
        return 0
    if n==1:
        return 1
    sum=fib(n-1,memo)+fib(n-2,memo)
    memo[n]=sum
    return memo[n]
memo={}
c=0
print(fib(100,memo))
print(c)
