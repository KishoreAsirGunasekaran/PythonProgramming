Check pair with difference k
Given an array A of sorted integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.
Input Format
1.      First line is number of test cases T. Following T lines contain:
2.      N, followed by N integers of the array
3.      The non-negative integer k
Output format
Print 1 if such a pair exists and 0 if it doesn’t
Input
1
3 
1 
3 
5
4
Output:
1
Input
1
3 
1 
3 
5
99
Output
0


For example:
Input	Result
1
3 
1 
3 
5
4
	   1
1
3 
1 
3 
5
99
     0

a=int(input())
while(a!=0):
    b=int(input())
    l=[]
    f=0
    for i in range(b):
        c=int(input())
        l.append(c)
    k=int(input())
    a-=1
    for i in range(b):
        for j in range(b):
            if(l[i]-l[j]==k and i!=j):
                f=1
                break
    if(f==1):
        print(1)
    else:
        print(0)


