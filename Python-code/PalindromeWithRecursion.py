#Palindrome using Recursion
import string
s=raw_input("Enter your input: ")
s1=s.lower()
#Recursion function to check palindrome
def ispal(s):
    if len(s)<=0:
        return True
    else:
        return s[0]==s[-1] and ispal(s[1:-1])
print ispal(s1)
    
