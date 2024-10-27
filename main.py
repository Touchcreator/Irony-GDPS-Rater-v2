import mysql.connector
from discord import SyncWebhook

db = mysql.connector.connect(
    host = "put-ur-own",
    user = "put-ur-own",
    passwd = "put-ur-own",
    database = "put-ur-own"
)

webhook = SyncWebhook.from_url("put-ur-own")

cursor = db.cursor()

levelID = input("What is the level's ID?")
difficulty = str(input("What difficulty?"))
difficultyNumb = 0

if difficulty == "Easy":
    difficultyNumb = 10
elif difficulty == "Normal":
    difficultyNumb = 20
elif difficulty == "Hard":
    difficultyNumb = 30
elif difficulty == "Harder":
    difficultyNumb = 40
elif difficulty == "Insane":
    difficultyNumb = 50
elif difficulty == "Demon":
    difficultyNumb = 50
    difficulty = "Demon (Insane in-game)"

toRun = "UPDATE levels SET starDifficulty = '" + str(difficultyNumb) + "', starFeatured = '2' WHERE levels.levelID = " + levelID

cursor.execute(toRun)
db.commit()

cursor.execute("SELECT userName FROM levels WHERE levels.levelID = " + levelID)
username = cursor.fetchone()
cursor.execute("SELECT levelName FROM levels WHERE levels.levelID = " + levelID)
levelname = cursor.fetchone()

print("Successfully rated \"" + levelname[0] + " by " + username[0] + "\" " + difficulty)

webhook.send("<@&1193324743978397826> \"" + levelname[0] + "\" by " + username[0] + " has been given a rating of " + difficulty + "!")

# UPDATE `levels` SET `starDifficulty` = '40', `starFeatured` = '1' WHERE `levels`.`levelID` = 5 
