n = int(input())

games = 0
gamesList = []
while games < n:
    gamesList.append(input().split(';'))
    games += 1

print(games)
print(gamesList)

tableResult = {}
for i in range(0, n):
    tableResult[gamesList[i][0]] = [0, 0, 0, 0, 0]
    tableResult[gamesList[i][2]] = [0, 0, 0, 0, 0]
    tableResult[gamesList[i][0]][0] += 1
    tableResult[gamesList[i][2]][0] += 1
    if gamesList[i][1] > gamesList[i][3]:
        tableResult[gamesList[i][0]][1] += 1
        tableResult[gamesList[i][0]][4] += 3
        tableResult[gamesList[i][2]][3] += 1
    elif gamesList[i][1] == gamesList[i][3]:
        tableResult[gamesList[i][0]][2] += 1
        tableResult[gamesList[i][2]][2] += 1
        tableResult[gamesList[i][0]][4] += 1
        tableResult[gamesList[i][2]][4] += 1
    elif gamesList[i][1] < gamesList[i][3]:
        tableResult[gamesList[i][2]][1] += 1
        tableResult[gamesList[i][2]][4] += 3
        tableResult[gamesList[i][0]][3] += 1


print(tableResult)


