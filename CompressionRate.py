class CompressionRate:

    #constructor
    def __init__(self, binAlphabet: dict, frequencies: dict, initialFile:str):
        self.binAlphabet = binAlphabet
        self.frequencies = frequencies
        self.initialFile = initialFile
        self.savedRatio = self.calculateRatio()

    #Getters

    #returns the binary alphabet
    def getBinAlphabet(self):
        return self.binAlphabet

    #returns the text frequencies
    def getFrequencies(self):
        return self.frequencies

    #returns the initial file
    def getInitialFile(self):
        return self.initialFile

    #returns the percentage of saved data
    def getSavedRatio(self):
        return self.savedRatio

    #returns the file compression ratio
    def calculateRatio(self):
        compresionCount = 0
        initialCount = len(self.getInitialFile())*8

        for caracter in self.getFrequencies():
            compresionCount += int(len(self.getBinAlphabet()[caracter[0]] * caracter[1]))
        print(compresionCount, initialCount)
        return 1 - float(compresionCount/initialCount)
