"""Q. Given an integer x, return true if x is a 
palindrome and false otherwise."""

x = int(input())

if x<0 or (x%10 == 0 and x!=0):
    print(False)
else:
    reverse = 0
    while x>reverse:
        reverse = reverse*10 + x%10
        x = x//10
    print(x==reverse or x==reverse//10)