# print("Enter no. to find the factorial.")
# num = int(input("enter the number :"))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print(fact)

def factorial(x):
    if x==1:
        return 1
    else:
        return x * factorial(x - 1)
number = int(input("Enter number :"))
result = factorial(number)
print(f"The factorial of {number} is {result}")
