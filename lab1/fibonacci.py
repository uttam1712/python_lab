n = int(input("Enter number: "))

t1 = 0
t2 = 1

print("Fibonacci series : ")
print(t1, "\n", t2)

for i in range(0, n-2):
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(t3, " ")