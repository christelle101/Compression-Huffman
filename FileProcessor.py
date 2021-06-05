class File:
    def __init__(self, filePath):
        #name of the file that is going to be processed
        self.filePath = filePath
    
    def getFileContent(self, filePath):
        #returns the content of the txt file
        return open(filePath).read()

    def ASCII_extractor(self, filePath):
        fileContent = self.getFileContent(filePath)
        for c in fileContent:
            return(c, ord(c))

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

    def dictionary(self, alphabet, frequency):
        #creation of a new dictionary
        dic = dict()
        for k in range(0, len(alphabet)):
            dic[frequency[k]] = alphabet[k]
        return dic

    def freqSort(self, dic):
        dicByFreq = {i: v for i, v in sorted(dic.items(), key=lambda item: item[1])}
        return dicByFreq

    def ASCIISort(self, dic):
        dicByASCII = dict()
        for k in sorted(dic.keys()):
            dicByASCII[k] = dic[k]
        return dicByASCII

    def freqThenASCII_sort(self, dic):
        return sorted(dic.items, key = lambda x: (x[1],x[0]))

    def writeFreqInFile(self, caracter, freq, fileName):
        with open(fileName[:4] + '_Freq.txt', 'a') as f:
            if (freq != None):
                f.write(caracter + '' + str(freq) + '\n')
            else:
                f.write(caracter + '\n')
        f.close()