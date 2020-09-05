from user import user

class circuitSwitching:
    def __init__(self, users, bandWidth):
        self.users = users
        self.bandWidth = bandWidth
        print("********* Comutação por circuitos *********")

    def calculateMaxUsersSuported(self):
        band = 0.0
        maxUsers = 0
        for i in self.users:
            band += i.requiredDataRate
            if(band > self.bandWidth):
                break
            maxUsers += 1
        return maxUsers        