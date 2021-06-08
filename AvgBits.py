class AverageStorageBits:

    def __init__(self, binAlphabet: dict, frequencies: dict, initialFile:str):
        self.binAlphabet = binAlphabet
        self.frequencies = frequencies
        self.initialFile = initialFile
        
    def getBinAlphabet(self):
        return self.binAlphabet

    def getFrequencies(self):
        return self.frequencies

    def getInitialFile(self):
        return self.initialFile

    def calculateAvgStorage(self):
        total = 0
        binTree = self.getBinAlphabet()
        for caracter in binTree.values():
            total += len(caracter)
        return (total/len(binTree))