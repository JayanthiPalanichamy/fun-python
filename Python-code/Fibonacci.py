#Fibonacci series
s=int(raw_input("Enter the fibonacci number to be found : "))

def fib(a):
  assert type(a)==int and a>=0
  if a==0 or a==1:
      return 1
  else:
      return fib(a-1)+fib(a-2)
print "The fibonacci series is"
for i in range(s):
    print fib(i)
    
   
      
