n, m = map(int, input().split())

if n < 0 and m < 0:
    print(abs(n-m))
elif n < 0 or m < 0:
    print(abs(n)+abs(m))
else:
    print(abs(n-m))