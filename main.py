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

levelID = input("What is the level's ID? ")
stars = input("How many stars? ")
feature = input("Feature? ")
difficultyNumb = 0

if stars == 1:
    difficulty = "Auto"
if stars == 2:
    difficulty = "Easy"
if stars == 3:
    difficulty = "Normal"
if stars == 4 or stars == 5:
    difficulty = "Hard"
if stars == 6 or stars == 7:
    difficulty = "Harder"
if stars == 8 or stars == 9:
    difficulty = "Insane"
if stars == 10:
    difficulty = "Demon"

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
elif difficulty == "Auto":
    difficultyNumb = 50
    
if difficulty != "Auto" and difficulty != "Demon":
    toRun = f"UPDATE 'levels' SET 'starDifficulty' = {difficultyNumb}, 'starFeatured' = {feature}, 'starStars' = {stars}, WHERE `levels`.`levelID` = {levelID} "
    
if difficulty == "Auto":
    toRun = f"UPDATE 'levels' SET 'starDifficulty' = {difficultyNumb}, 'starFeatured' = {feature}, 'starStars' = {stars}, 'starAuto' = 1, WHERE `levels`.`levelID` = {levelID} "

if difficulty == "Demon":
    toRun = f"UPDATE 'levels' SET 'starDifficulty' = {difficultyNumb}, 'starFeatured' = {feature}, 'starStars' = {stars}, 'starDemon' = 1, WHERE `levels`.`levelID` = {levelID} "

cursor.execute(toRun)
db.commit()

cursor.execute("SELECT userName FROM levels WHERE levels.levelID = " + levelID)
username = cursor.fetchone()
cursor.execute("SELECT levelName FROM levels WHERE levels.levelID = " + levelID)
levelname = cursor.fetchone()

print("Successfully rated \"" + levelname[0] + " by " + username[0])

webhook.send("<@&1193324743978397826> \"" + levelname[0] + "\" by " + username[0] + " has been given " + str(stars) + " stars!")

# UPDATE `levels` SET `starDifficulty` = '40', `starFeatured` = '1' WHERE `levels`.`levelID` = 5 
