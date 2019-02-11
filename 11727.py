size = int(input())
for i in range(size):
    values = sorted([int(n) for n in input().split(" ")])
    print("Case {}: {}".format(i+1, values[1]))
