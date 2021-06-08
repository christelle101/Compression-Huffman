class AverageStorageBits:

    #constructor
    def __init__(self, binAlphabet: dict, frequencies: dict, initialFile:str):
        self.binAlphabet = binAlphabet
        self.frequencies = frequencies
        self.initialFile = initialFile
    
    #returns the binary alphabet
    def getBinAlphabet(self):
        return self.binAlphabet

    #returns the text frequencies
    def getFrequencies(self):
        return self.frequencies

    #returns the initial file
    def getInitialFile(self):
        return self.initialFile

    #returns the average number of storage bits
    def calculateAvgStorage(self):
        total = 0
        binTree = self.getBinAlphabet()
        for caracter in binTree.values():
            total += len(caracter)
        return (total/len(binTree))
