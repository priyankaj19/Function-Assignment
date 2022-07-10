# WAP to print the following fibonacci series using functons:
# 1 1 2 3 5 8 ......n terms

# 1) with i/p no o/p
def fibo(a,b,n):
    print("Fibonacci Series: ")
    for i in range(1,n+1):
        c=a+b
        print(c,end=" ")
        a=b
        b=c

n = int(input("Enter number of terms: "))
fibo(1,0,n)

# 2) no i/p no o/p
def fibo(a,b):
    n = int(input("Enter number of terms: "))
    print("Fibonacci Series: ")
    for i in range(1,n+1):
        c=a+b
        print(c,end=" ")
        a=b
        b=c

fibo(1,0)

# OR

# Using recursion
def fibo(a,b,n):
    if (n==0):
        return
    else:
        c=a+b
        print(c, end=" ")
        return fibo(b,c,n-1)

n=int(input("Enter the number: "))
fibo(1,0,n)