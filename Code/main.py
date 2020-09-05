from packetSwitching import packetSwitching
from circuitSwitching import circuitSwitching
from user import user

class main:

    def main():
        users = []
        for i in range(0, 4):
            users.append(user(30, .5))

        users.append(user(20, .0))
        users.append(user(4, .3))
        circ = circuitSwitching(users, 400.0)
        
    if __name__ == "__main__":
       main() 