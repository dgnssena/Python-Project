

n = int(input("please enter n number "))
m = int(input("please enter n number "))

n1, n2 = 0, 1
counter = 0
factorial = 1
#nterms=0

# ackermann
def A(m, n, s="% s"):
    print(s % ("A(% d, % d)" % (m, n)))
    if m == 0:
        return n + 1
    if n == 0:
        return A(m - 1, 1, s)
    n3 = A(m, n - 1, s % ("A(% d, %% s)" % (m - 1)))
    return A(m - 1, n3, s)


dosya = open("data.txt", "a")
result = str(A(n, m))
dosya.write('Ackermann ' + '=' +result + '\n')
print(A(n, m))

# fibonacci
if n <= 0:
    print("n number must be positive!")

elif n == 1:
    print("Fibonacci ", "=")
    print(n1)

else:
    print("Fibonacci =")

    while counter < n:
        print(n1)

        nth = n1 + n2

        n1 = n2
        n2 = nth
        counter += 1
        resultFib = str(n1)

dosya.write('Fibonacci ' + '=' + resultFib + '\n')
#resultFib = str(nterms)


# factorial
if n < 0:
    print("n number must be positive!")
else:
    for i in range(1, n + 1):
        factorial = factorial * i

    print("The factorial ", n, "is", factorial)
    resultFact = str(factorial)
    dosya.write('Factorial ' + '=' + resultFact + '\n')
