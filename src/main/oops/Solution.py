testcase = int(input())
dict = {'E': [1, 0], 'N': [0, 1], 'W': [-1, 0], 'S': [0, -1]}
t = 1
while t <= testcase:
    inp = input().split()
    x = int(inp[0])
    y = int(inp[1])
    move = inp[2]
    move = list(move)
    result = 0
    flag = True
    for l in range(len(move)):
        x, y = x + dict[move[l]][0], y + dict[move[l]][1]
        tempSum = abs(x) + abs(y)
        result += 1
        # print(ans, tempSum)
        if tempSum <= result:
            print("Case #" + str(t) + ': ' + str(result))
            flag = False
            break

    if flag:
        print("Case #" + str(t) + ': ' + 'IMPOSSIBLE')
    t += 1
