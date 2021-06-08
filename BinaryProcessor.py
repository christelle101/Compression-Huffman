class BinaryProcess:

    #returns the binary code
    def BinConvert(self, content, binTable):
        binContent = ""
        for i in content:
            binContent = binContent + binTable[i]
        return binContent

    #add the missing bits when the length of the binary code is inferior to 8 (to make an octet)
    def completeBinCode(self, content):
        while len(content)%8 != 0:
            content = content + "0"

    #returns a list of the binary codes associated with the caracters
    def createBinList(self, content):
        BinList = []
        for i in range (8, len(content), 8):
            BinList.append(content[i-8:i])
        return BinList

    #creates a bin file
    def writeBinFile(self, fileName, content):
        with open(fileName, "wb") as f:
            for i in content:
                f.write((int(i, base=2)).to_bytes((len(i)//8), byteorder='big'))
        f.close()
    
    #writes a txt file containing the binary codes assigned to each caracter
    def writeBinCodes(self, alphabet, binTable, fileName):
        with open(fileName[:4]+'_BinCodes.txt','a') as f:
            for i in alphabet:
                f.write("The binary code of " + i + "is : " + str(binTable[i]) + '\n')
            f.close()



