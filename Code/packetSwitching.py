from combinatorics import combinatorics

class packetSwitching:

    def __init__(self, users, bandWidth):
        self.users = users
        self.users.sort(key = lambda u:u.requiredDataRate)
        self.bandWidth = bandWidth
        print("********* Comutação por pacotes ********")

    def getUserThreshold(self):
        band = 0.0
        userThreshold = 0
        for i in self.users:
            band += i.requiredDataRate
            userThreshold += 1
            if(band > self.bandWidth):
                break
        return userThreshold  
    
    def getBottleneckProbability(self):
        probability = 0.0
        userThreshold = self.getUserThreshold()
        userCount = self.users.__len__()

        for i in range(userThreshold - 1, userCount):
            active = (self.users[i].activeProbability ** (i + 1))
            inactive = (self.users[i].inactiveProbability ** (userCount - (i + 1)))
            combination = (combinatorics.combination(userCount, i + 1))
            probability += combination * active * inactive
        return probability

    def getProbabilityByUser(self):
        probabilities = []
        userCount = self.users.__len__()

        for i in range(0, userCount):
            active = (self.users[i].activeProbability ** (i + 1))
            inactive = (self.users[i].inactiveProbability ** (userCount - (i + 1)))
            combination = (combinatorics.combination(userCount, i + 1))
            probability = combination * active * inactive
            probabilities.append(probability)
        return probabilities