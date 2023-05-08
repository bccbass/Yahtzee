# create a new player log class to store game history and save in JSON file
# Name
# list of scores
# Date of game played? This may be excessive. 
# highest score/highest score method
# global highest score

class PlayerLog:
    all_time_high = 0 #This will be global to the PlayerLog class and should be updated as PlayerLog.all_time_high = new high score
    def __init__(self, name):
        self.name = name
        is_champion = False
        self.high_score = 0
        self.score_history = [] #save this in list for now. Possibly add date in the future - key = score, date = value?

