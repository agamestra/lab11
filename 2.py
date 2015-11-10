from Point import*
N=input(int())
max=Point(input())
for i in range (N):
    a=Point(input())
    if a>max:
        max=a
print (max)