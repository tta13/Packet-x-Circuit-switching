from packetSwitching import packetSwitching
from circuitSwitching import circuitSwitching
from combinatorics import combinatorics
from user import user

class main:

    def main():
        userAmount = int(input("Digite a quantidade de usuários: "))
        activeChance = float(input("Digite a probabilidade de o usuário estar ativo: "))
        userBand = float(input("Digite a quantidade de dados (em kbps) requisitada por cada usuário: "))
        linkBand = float(input("Digite a capacidade total do enlace (em kbps): "))

        users = []
        for i in range(0, userAmount):
           users.append(user(userBand, activeChance))
        
        users.sort(key = lambda u:u.requiredDataRate)

        circuit = circuitSwitching(users, linkBand)
        max = circuit.calculateMaxUsersSuported()
        print("Número máximo de usuários conectados ", max)

        packet = packetSwitching(users, linkBand)
        prob = packet.getBottleneckProbability()
        print("Probabilidade da demanda superar a capacidade do enlace ", prob)

    if __name__ == "__main__":
       main() 