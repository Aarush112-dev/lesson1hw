question = input("Which type of algorthm would you like to calculate the sum of n numbers for? \npress a for linear \npress b for quadratic\n")
n = int(input("Choose a number at which the algorithm will end at: "))

def linear(n):
    answer = n*(n+1)//2
    print(answer)

def quadratic(n):
    answer = n*(n+1)*(2*n+1)//6
    print(answer)

if question == "a":
    linear(n)

elif question == "b":
    quadratic(n)





