size = int(input())
cases = []
for i in range(size):
    cases.append([int(n) for n in input().split(" ")])

for c in cases:
    if c[0] > c[1]:
        print(">")
    if c[0] < c[1]:
        print("<")
    if c[0] == c[1]:
        print("=")
