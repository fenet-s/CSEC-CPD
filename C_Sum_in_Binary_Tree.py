t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    while n >= 1:
        ans += n
        n //= 2
    print(ans)
