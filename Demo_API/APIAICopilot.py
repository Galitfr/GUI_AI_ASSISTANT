#This program will demonstrate the work with GitHub API and API.AI
#It will take the user's input and will return the number of repositories the user has on GitHub
#It will also return the list of repositories the user has on GitHub

# a function calculating the nth Fibonacci number
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# main - the program's entry point
n = input("Enter the number of Fibonacci numbers you want to calculate: ")
print("The first", n, "Fibonacci numbers are:")
for i in range(int(n)):
    print(fibonacci(i))
    
