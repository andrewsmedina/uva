while True:
    queries = int(input())
    if queries == 0:
        break

    division_point = [int(n) for n in input().split(" ")]
    for i in range(queries):
        query = [int(n) for n in input().split(" ")]
        if query[0] == division_point[0] or query[1] == division_point[1]:
            print("divisa")
        if query[0] < division_point[0] and query[1] > division_point[1]:
            print("NO")
        if query[0] < division_point[0] and query[1] < division_point[1]:
            print("SO")
        if query[0] > division_point[0] and query[1] > division_point[1]:
            print("NE")
        if query[0] > division_point[0] and query[1] < division_point[1]:
            print("SE")

