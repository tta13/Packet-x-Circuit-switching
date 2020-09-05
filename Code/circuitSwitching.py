from user import user

class circuitSwitching:
    def calculateMaxUsersSuported():
        band = 0.0
        maxUsers = 0
        for i in users:
            band += users.requiredData
            if(band > bandWidth):
                break
            maxUsers += 1
        return maxUsers




    def __init__(self, users, bandWidth):
        self.users = users
        self.users.sort(key = lambda u:u.requiredDataRate)
        self.bandWidth = bandWidth