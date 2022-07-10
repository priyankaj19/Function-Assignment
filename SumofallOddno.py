# Sum of all odd numbers between 1 to n.

# 1) with i/p with o/p
def sum_of_odd(n):    # sum of odd number
    sum=0
    for i in range(1,n+1,2):
        sum+=i
    return sum

n = int(input("Enter the number: "))
print("sum of odd numbers: ",sum_of_odd(n))

# 2) with i/p no o/p
def sum_of_odd(n):    # sum of odd number
    sum=0
    for i in range(1,n+1,2):
        sum+=i
    print("sum of odd numbers: ",sum)

n = int(input("Enter the number: "))
sum_of_odd(n)

# 3) no i/p with o/p
def sum_of_odd():    # sum of odd number
    n = int(input("Enter the number: "))
    sum=0
    for i in range(1,n+1,2):
        sum+=i
    return sum

print("sum of odd numbers: ",sum_of_odd())

# 4) no i/p no o/p
def sum_of_odd():    # sum of odd number
    n = int(input("Enter the number: "))
    sum=0
    for i in range(1,n+1,2):
        sum+=i
    print("sum of odd number: ",sum)

sum_of_odd()

# OR
# 1) with i/p with o/p
def sum_of_odd(n):    # sum of odd number
    sum=0
    for i in range(1,n+1):
        if(i%2 != 0):
            sum+=i
    return sum

n = int(input("Enter the number: "))
print("sum of odd numbers: ",sum_of_odd(n))

# 2) with i/p no o/p
def sum_of_odd(n):    # sum of odd number
    sum=0
    for i in range(1,n+1):
        if(i%2 != 0):
            sum+=i
    print("sum of odd numbers: ",sum)

n = int(input("Enter the number: "))
sum_of_odd(n)

# 3) no i/p with o/p
def sum_of_odd():    # sum of odd number
    n = int(input("Enter the number: "))
    sum=0
    for i in range(1,n+1):
        if(i%2 != 0):
            sum+=i
    return sum

print("Sum of odd number: ",sum_of_odd())

# 4) no i/p no o/p
def sum_of_odd():    # sum of odd number
    n = int(input("Enter the number: "))
    sum=0
    for i in range(1,n+1):
        if(i%2 != 0):
            sum+=i
    print("sum of odd numbers: ",sum)

sum_of_odd()