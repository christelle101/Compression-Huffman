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

    def createBinList(self, content):
        BinList = []
        for i in range (8, len(content), 8):
            BinList.append(content[i-8:i])
