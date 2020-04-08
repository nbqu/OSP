n = int(input("fibonacci number? : "))
fib = [0, 1, 1]
for i in range(3, n+1):
    fib.append(fib[i-1]+fib[i-2])

for i in range(1, n):
    print(fib[i], end=', ')
print(fib[n])
print("F%d = %d" % (n, fib[n]))
