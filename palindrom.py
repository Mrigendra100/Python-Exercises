# Python program to find string is palindrom or not?

input = "abcbdasasa"

def palindrome(a):
    length = len(a)
    reversed = "" 

    while (length > 0):
        reversed = reversed + a[length-1]
        length= length -1

    print(a)
    print(reversed)

    if(a == reversed):
        return("It is a palindrom")
    else:
        return("It is not a palindrom") 





print(palindrome(input))

print(palindrome('amaama'))

    



