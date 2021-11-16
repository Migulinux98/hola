# #Python programs
# ##list, functions
```PYTHON
#######Primes numbers##########

nums = [1, 2, 3, 4, 5]
def square(n):
    return n*n

result = map(square, nums)
print (list(result))

#lambda
result = map(lambda x: x*x*x, nums)
print (list(result))

#map and lambda
nums1 = [12, 13, 14]
nums2 = [1, 2, 3]
result = map(lambda x, y: x * y, nums1, nums2)
print(list(result))

#list comprehension
squares = [a**2 for a in range(5)]
print(squares) 
```
```PYTHON
###########Palindrome###########

def is_palindrome(s):
    if s==s[::-1]:
        return True
    else:
        return False

polin = []
maxi=0
for i in range (100, 1000):
    for j in range (100, 1000):
        num = i*j 
        x=str(num)
        if (is_palindrome(x)):
            polin.append(num)
            if maxi < num:
                maxi = num
        
print(polin)

print('The maximun palindrome is:', max(polin))
print(maxi)
```