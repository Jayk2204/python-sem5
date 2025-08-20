players = {}

n = int(input("Enter number of players: "))

for i in range(n):
    name = input("Enter player name: ")
    score = int(input("Enter score: "))
    players[name] = score

search = input("Enter player name to get score: ")

if search in players:
    print(search, "scored", players[search], "runs")
else:
    print("Player not found")
