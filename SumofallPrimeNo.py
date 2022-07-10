# Sum of all prime numbers between 1 to n.

# 1) with i/p with o/p
def sum_of_prime(n):         # sop - sum of prime number
    sum=0
    for i in range(2,n+1):
        for j in range(2,i):
            if (i%j == 0):
                break
        else:
            sum+=i
    return sum

n = int(input("Enter the number: "))
print("sum of prime numbers: ",sum_of_prime(n))

# 2) with i/p no o/p
def sum_of_prime(n):         # sop - sum of prime number
    sum=0
    for i in range(2,n+1):
        for j in range(2,i):
            if (i%j == 0):
                break
        else:
            sum+=i
    print("sum of prime number: ",sum)

n = int(input("Enter the number: "))
sum_of_prime(n)

# 3) no i/p with o/p
def sum_of_prime():         # sop - sum of prime number
    n = int(input("Enter the number: "))
    sum=0
    for i in range(2,n+1):
        for j in range(2,i):
            if (i%j == 0):
                break
        else:
            sum+=i
    return sum

print("sum of prime numbers: ",sum_of_prime())

# 4) no i/p no o/p
def sum_of_prime():         # sop - sum of prime number
    n = int(input("Enter the number: "))
    sum=0
    for i in range(2,n+1):
        for j in range(2,i):
            if (i%j == 0):
                break
        else:
            sum+=i
    print("sum of prime numbers: ",sum)

sum_of_prime()

# OR

def sop(n):
        for j in range(2,n):
            if (n%j == 0):
                return 0
        else:
            return n

n = int(input("Enter the number: "))
sum = 0
for i in range(2,n+1):
    sum+=sop(i)
print("sumation: ",sum)