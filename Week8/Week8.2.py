Check Pair
Given a tuple and a positive integer k, the task is to find the count of distinct pairs in the tuple whose sum is equal to K.
Examples:
Input: t = (5, 6, 5, 7, 7, 8 ), K = 13 
Output: 2 
Explanation: 
Pairs with sum K( = 13) are  {(5, 8), (6, 7), (6, 7)}. 
Therefore, distinct pairs with sum K( = 13) are { (5, 8), (6, 7) }. 
Therefore, the required output is 2.

For example:
Input	Result
1,2,1,2,5
3	1
1,2
0	0

t = input()
k = int(input())
a = t.split(",")
l = [int(x) for x in a]
count = 0
x = set()
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] + l[j] == k:
            s = (l[i], l[j])
            if s not in x and (l[j], l[i]) not in x:
                count += 1
                x.add(s)

print(count)


