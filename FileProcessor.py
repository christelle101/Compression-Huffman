class FileProcess:

    """Constructeur de la classe FileProcess.
    Mis en commentaire par la suite car il imposait une contrainte supplementaire dans les autres classes.
    """
    #def __init__(self, filePath):
        #name of the file that is going to be processed
    #  self.filePath = filePath

    """Retourne le contenu d'un fichier dont le nom est en parametre.
    Fonctions utilisées:
        - open() : ouvre filePath et donne un objet fichier correspondant
        - read() : renvoie le nombre d'octets associés au fichier
    """
    #takes in parameter a file path and returns the content of the file
    def getFileContent(self, filePath):
        return open(filePath).read()

    """Renvoie tous les caracteres du fichier couples a leur code ASCII.
        - ord() : renvoie l'entier representant l'Unicode du caractere
    """
    #returns each caracter and its ASCII code
    def ASCII_extractor(self, filePath):
        fileContent = self.getFileContent(filePath)
        for c in fileContent:
            print(c, ord(c))

    """Retourne l'alphabet associe au texte ainsi que la frequence de chaque caractere.
    """
    #returns the alphabet and the caracters' individual frequency in a txt file
    def getAlphabetandFreq(self, filePath):
        fileContent = self.getFileContent(filePath)
        alphabet = []
        frequency = []
        for i in range(0, len(fileContent)):
            if fileContent[i] not in alphabet:
                alphabet.append(fileContent[i])
                frequency.append(1)
            else:
                position = alphabet.index(fileContent[i])
                frequency[position] = frequency[position] + 1
        return alphabet, frequency

    """Prend en parametre l'alphabet et la frequence et retourne un dictionnaire dic.
    """
    #returns a dictionary that contains the alphabet and the caracters' individual frequency
    def dictionary(self, alphabet, frequency):
        #creation of a new dictionary
        dic = dict()
        for k in range(0, len(alphabet)):
            dic[frequency[k]] = alphabet[k]
        return dic

    """Effectue un tri du dictionnaire passé en paramètre.
    Le tri est d'abord réalisé par fréquence puis par code ASCII.
    """
    #sorts the newly created dictionary by frequency, then by ASCII code
    def freqThenASCII_sort(self, dic):
        return sorted(dic.items(), key = lambda x: (x[1],x[0]))
    
    """Crée un nouveau fichier txt qui se terminera par _Frequency.
    """
    #creates a new txt file that contains each caracter and its frequency
    def writeFreqInFile(self, caracter, freq, fileName):
        with open(fileName[:4] + '_Frequency.txt', 'a') as f:
            if (freq != None):
                f.write(caracter + '' + str(freq) + '\n')
            else:
                f.write(caracter + '\n')
        f.close()