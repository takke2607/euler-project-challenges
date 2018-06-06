fibo = []
efibo = []
def even_fibo(n):
    if n <= 1:
        return n
    else:
        return even_fibo(n-1) + even_fibo(n-2)

num = input("Enter number of terms:")
print "Fibbonaci series:"
for i in range(num):
    fibo.append(even_fibo(i))
for n in fibo:
    if n % 2 == 0:
        efibo.append(n)
print fibo
print "sum of even fibo numbers: %d"%(sum(efibo))

    
    
