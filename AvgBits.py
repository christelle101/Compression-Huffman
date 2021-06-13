class AverageStorageBits:

    """ Constructeur de la classe AverageStorageBits.
    -   binAlphabet : alphabet binaire
    -   frequencies : fréquences d'apparition
    -   initialFile : fichier initial
    """
    #constructor
    def __init__(self, binAlphabet: dict, frequencies: dict, initialFile:str):
        self.binAlphabet = binAlphabet
        self.frequencies = frequencies
        self.initialFile = initialFile
    
    """ Retourne l'alphabet binaire.
    """
    #returns the binary alphabet
    def getBinAlphabet(self):
        return self.binAlphabet

    """ Retourne les fréquences d'apparition.
    """
    #returns the text frequencies
    def getFrequencies(self):
        return self.frequencies

    """ Retourne le fichier initial.
    """
    #returns the initial file
    def getInitialFile(self):
        return self.initialFile

    """ Retourne le nombre moyen de bits de stockage.
    """
    #returns the average number of storage bits
    def calculateAvgStorage(self):
        total = 0
        binTree = self.getBinAlphabet()
        for caracter in binTree.values():
            total += len(caracter)
        return (total/len(binTree))