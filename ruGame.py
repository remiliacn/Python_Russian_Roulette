import random, time

class russianRoulette:
    def __init__(self):
        self.gameDict = {

        }

    def setUpDictByGroup(self, user_id):
        self.gameDict[user_id] = {
            "theLowerBound": 1,
            "theHighestBound": 8,
            "theLastDeath": 1,
            "playerDict" : {}
        }

    def addPlayerIn(self, group_id, user_id):
        self.gameDict[group_id]["playerDict"][user_id] = 1

    def addPlayerPlayTime(self, group_id, user_id):
        self.gameDict[group_id]["playerDict"][user_id] += 1

    def getPlayTimeWithUserId(self, group_id, user_id):
        return self.gameDict[group_id]["playerDict"][user_id]

    def pullTrigger(self, group_id):
        self.gameDict[group_id]["theLowerBound"] += 1
        self.gameDict[group_id]["theLastDeath"] += 1

    def getRestBullets(self, group_id):
        return self.gameDict[group_id]["theHighestBound"] - self.gameDict[group_id]["theLowerBound"]

    def getDeath(self, group_id):
        lastDeath = self.gameDict[group_id]["theLastDeath"]
        self.gameDict[group_id]["theLastDeath"] = 1
        return lastDeath

    def getResult(self, group_id):
        random.seed(time.time_ns())
        draw = random.randint(self.gameDict[group_id]["theLowerBound"], self.gameDict[group_id]["theHighestBound"])
        if draw >= 8:
            self.gameDict[group_id]["theLowerBound"] = 1
            return True

        self.pullTrigger(group_id)
        return False
