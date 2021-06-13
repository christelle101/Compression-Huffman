class CompressionRate:

    """ Constructeur de la classe CompressionRate.
    -   binAlphabet : alphabet binaire
    -   frequencies : fréquences
    -   initialFile : fichier initial
    -   savedRatio : taux d'espace gagné
    """
    #constructor
    def __init__(self, binAlphabet: dict, frequencies: dict, initialFile:str):
        self.binAlphabet = binAlphabet
        self.frequencies = frequencies
        self.initialFile = initialFile
        self.savedRatio = self.calculateRatio()

    """ Getters et setters.
    Fonctions qui permettent la modification et l'accession de certains attributs de l'objet.
    """

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

    """ Retourne le taux de données gagnées.
    """
    #returns the percentage of saved data
    def getSavedRatio(self):
        return self.savedRatio

    """ Retourne le taux de compression personnalisé pour un fichier donné
    """
    #returns the file compression ratio
    def calculateRatio(self):
        compresionCount = 0
        initialCount = len(self.getInitialFile())*8

        for caracter in self.getFrequencies():
            compresionCount += int(len(self.getBinAlphabet()[caracter[0]] * caracter[1]))
        print(compresionCount, initialCount)
        return 1 - float(compresionCount/initialCount)
