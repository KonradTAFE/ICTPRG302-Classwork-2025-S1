import datetime
current_time = datetime.datetime.now()
timestamp = current_time.strftime("%d-%m-%Y %H:%M:%S")

player_score = input("Enter your latest score: ")
filehandle = open("scores.txt", "a")
filehandle.write(f"\n{player_score} recorded at: {timestamp}")
filehandle.close()