# WAP to print following series:
# a) 1! + 2! + 3! +4! +........n!

# 1) with i/p with o/p
def sum_of_fact(n):    # sum of factoral series
    sum = 0
    fact = 1
    for i in range(1,n+1):
        fact*=i
        sum += fact
    return sum

n = int(input("Enter the number: "))
print("Factorial summation: ",sum_of_fact(n))

# 2) with i/p no o/p
def sum_of_fact(n):    # sum of factoral series
    sum = 0
    fact = 1
    for i in range(1,n+1):
        fact*=i
        sum += fact
    print("Factorial summation: ",sum)

n = int(input("Enter the number: "))
sum_of_fact(n)

# 3) no i/p with o/p
def sum_of_fact():    # sum of factoral series
    n = int(input("Enter the number: "))
    sum = 0
    fact = 1
    for i in range(1,n+1):
        fact*=i
        sum += fact
    return sum

print("Factorial summation: ",sum_of_fact())

# 4) no i/p no o/p
def sum_of_fact():    # sum of factoral series
    n = int(input("Enter the number: "))
    sum = 0
    fact = 1
    for i in range(1,n+1):
        fact*=i
        sum += fact
    print("Factorial summation: ",sum)

sum_of_fact()

# OR

def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f

n = int(input("Enter the number: "))
print("factorial: ",fact(n))
sum = 0
for i in range(1,n+1):
    sum+= fact(i)

print("factorial summation: ",sum)
