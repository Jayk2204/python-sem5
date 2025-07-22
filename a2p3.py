# Create a dictionary that will accept cricket players name and scores in a match. Also
# we are retrieving runs by entering the player’s name.
players = {}
n = int(input("Enter number of players: "))

for i in range(n):
    name = input("Enter player name: ")
    score = int(input("Enter score: "))
    players[name] = score
print(players)

search = input("Enter player name to get score: ")

if search in players:
    print("Score of", search, "is", players[search])
else:
    print("Player not found.")
