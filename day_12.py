for i in range(1,50):
    #print(i)
    for j in range(2,i):

        if i % j== 0:
            break
    else:

        print(i)

"""# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Print prime numbers between 1 and 5
print("Prime numbers between 1 and 5:")
for num in range(1, 6):
    if is_prime(num):
        print(num)"""