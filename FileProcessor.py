class FileProcess:
    #def __init__(self, filePath):
        #name of the file that is going to be processed
    #  self.filePath = filePath

    #takes in parameter a file path and returns the content of the file
    def getFileContent(self, filePath):
        return open(filePath).read()

    #returns each caracter and its ASCII code
    def ASCII_extractor(self, filePath):
        fileContent = self.getFileContent(filePath)
        for c in fileContent:
            print(c, ord(c))

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

    #returns a dictionary that contains the alphabet and the caracters' individual frequency
    def dictionary(self, alphabet, frequency):
        #creation of a new dictionary
        dic = dict()
        for k in range(0, len(alphabet)):
            dic[frequency[k]] = alphabet[k]
        return dic

    #returns the newly created dictionary sorted by caracter frequency
    def freqSort(self, dic):
        dicByFreq = {i: v for i, v in sorted(dic.items(), key=lambda item: item[1])}
        return dicByFreq

    #returns the newly created dictionary sorted by ASCII code
    def ASCIISort(self, dic):
        dicByASCII = dict()
        for k in sorted(dic.keys()):
            dicByASCII[k] = dic[k]
        return dicByASCII

    #sorts the newly created dictionary by frequency, then by ASCII code
    def freqThenASCII_sort(self, dic):
        return sorted(dic.items(), key = lambda x: (x[1],x[0]))

    #creates a new txt file that contains each caracter and its frequency
    def writeFreqInFile(self, caracter, freq, fileName):
        with open(fileName[:4] + '_Frequency.txt', 'a') as f:
            if (freq != None):
                f.write(caracter + '' + str(freq) + '\n')
            else:
                f.write(caracter + '\n')
        f.close()