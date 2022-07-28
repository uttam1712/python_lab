n = int(input("Enter number : "))
isPrime = True

if n == 1:
    print("Not Prime")
else:
    for i in range(2, (n//2)+1):
        if n%i == 0:
            isPrime = False
            break
    if isPrime:
        print("Prime")
    else: 
        print("Not prime")
