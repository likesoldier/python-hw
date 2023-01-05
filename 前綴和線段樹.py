t = int(input())
num_arr = [int(num_str) for num_str in input().split(' ')]
q = int(input())
for i in range(q):
    q_range = [int(num_str) for num_str in input().split(' ')]
    sum = 0
    for j in range(q_range[0]-1 , q_range[1]):
       sum  += num_arr[j]
    print(sum)