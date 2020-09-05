class user:
    def __init__(self, requiredDataRate, activeProbability):
        self.requiredDataRate = requiredDataRate
        self.activeProbability = activeProbability
        self.inactiveProbability = 1 - activeProbability

        print("Novo usuário criado com {} kbps de dados necessários".format(self.requiredDataRate) +
        " {} de chance de estar ativo e {} de chance de estar inativo"
        .format(self.activeProbability, self.inactiveProbability))