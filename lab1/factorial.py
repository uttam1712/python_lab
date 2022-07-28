def factorial(num):
    if num == 1:
        return 1
    
    return num * factorial(num-1)

n = int(input("Enter number: "))

ans = factorial(n)

print(n, "! =", ans)