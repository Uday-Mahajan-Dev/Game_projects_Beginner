import random
import mysql.connector

#connecting to mysql
mydb = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password = "*********",
    database = "Game_Demo"
)
mycursor = mydb.cursor()

print("Welcome to the Dragon Battle game")

player_name = input("Enter your player name : ")
level = 1
score = 0

#looping the game
for battle in range(1, 4):
    print(f"\n Battle {battle} begins !$")
    
    player_attack = random.randint(5, 15)
    monster_attack = random.randint(5, 15)
    
    print(f"You attack for {player_attack} damage!")
    print(f"Monster attacks for {monster_attack} damage!")
    
    if player_attack > monster_attack:
        print("You WIN this Battle!")
        score += 100
        level += 1
    else:
        print("You Lose! you piece of shit##")
        score += 50
    
print("\n Game over!")
print(f"Player: {player_name}, Level: {level}, Score: {score}")

#saving data into DB
sql = "INSERT INTO players (player_name, level, score) VALUES (%s, %s, %s)"
val = (player_name, level, score)
mycursor.execute(sql, val)
mydb.commit()

print("\n Your progress has been saved!")

#show all players
print("\n Leaderboard: ")
mycursor.execute("SELECT player_name, level, score FROM players ORDER BY score DESC")
players = mycursor.fetchall()

for p in players:
    print(f"Player: {p[0]}, Level: {p[1]}, Score: {p[2]}")
    