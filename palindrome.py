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