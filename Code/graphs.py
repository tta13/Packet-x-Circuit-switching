from matplotlib import pyplot as plt

class graphs:

    def __init__(self, title, xLabel, yLabel, path):
        self.title = title
        self.xLabel = xLabel
        self.yLabel = yLabel
        self.path = path

    def plotGraph(self, listX, listY, style, marker):
        plt.style.use("fivethirtyeight")
        plt.plot(listX, listY, linestyle = style, marker = marker)
        plt.xlabel(self.xLabel)
        plt.ylabel(self.yLabel)
        plt.title(self.title)
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(self.path) 
        print("Grafo salvo em " + self.path)
        plt.show()
        plt.close()