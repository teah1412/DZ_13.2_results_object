import random
import json
import datetime

# klasa
class Result:
    def __init__(self, attempts, player_name, date):
        self.attempts = attempts
        self.player_name = player_name
        self.date = date

# postavljam varijable
current_time = datetime.datetime.now()
secret = random.randint(1, 30)
attempts = 0


# otvaram dokument... nešto ne funkkcionira kada u dokumentu ima barem jedan rezultat?
with open("results.txt", "r") as score_file:
    results = json.loads(score_file.read())

for score_dict in results:
    print(str(score_dict["attempts"]) + " attempts, player: ", str(score_dict["player_name"]) + ", date: " + score_dict.get("date"))


# pitam ime
name = input("Please state your name for the score list: ")

# počinjem igru
while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        new_score = Result(attempts=attempts, player_name=name, date=str(datetime.datetime.now()))

        results.append(new_score.__dict__)

        with open("results.txt", "w") as score_file:
            score_file.write(json.dumps(results))

        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        print("Score stored in score list.")

        with open("results.txt", "w") as score_file:
            score_file.write(str(new_score.__dict__))

        break

    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
