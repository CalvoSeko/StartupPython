#python for finding the factorial
number=int(input())
result=1
while number!=0:
    result=result*number
    number=number-1
print(result)