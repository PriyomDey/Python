#write a program to print all natural nos. in reverse.

# n=int(input("Enter the total no. of natural nos. to be reversed: "))

# i=n
# while i>=1:
#  i=i-1
    
#  print(i)

n=int(input("Enter the total no. of natural nos. to be reversed: "))
for i in range(n,0,-1):
    print(i)
