class BinaryProcess:

    """ Convertit en code binaire.
    """
    #returns the binary code
    def BinConvert(self, content, binTable):
        binContent = ""
        for i in content:
            binContent = binContent + binTable[i]
        return binContent

    """ Complète le code binaire avec les bits manquants.
    Lorsque le code est insuffisant pour faire un octet, rajoute 0.
    """
    #add the missing bits when the length of the binary code is inferior to 8 (to make an octet)
    def completeBinCode(self, content):
        while len(content)%8 != 0:
            content = content + "0"

    """ Retourne une liste de codes binaires associée aux caractères
    """
    #returns a list of the binary codes associated with the caracters
    def createBinList(self, content):
        BinList = []
        for i in range (8, len(content), 8):
            BinList.append(content[i-8:i])
        return BinList

    """ Crée un fichier binaire dans le répertoire du projet.
    Fonctions utilisées :
    -   open() : ouvre fileName et retourne un objet fichier correspondant
    - write() : écrit les données
    Le paramètre "wb" indique que le fichier est ouvert pour une écriture en mode binaire.
    """
    #creates a bin file
    def writeBinFile(self, fileName, content):
        with open(fileName, "wb") as f:
            for i in content:
                f.write((int(i, base=2)).to_bytes((len(i)//8), byteorder='big'))
        f.close()

    """ Crée un fichier au format qui contient les codes binaires associés aux caractères.
    Fonctions utilisées :
    -   open() : ouvre fileName et donne un fichier correspondant
    -   close() : ferme le fichier ouvert
    Ouverture en mode 'a' : mode append pour l'addition de données, crée le fichier si il n'existe pas.
    """
    #writes a txt file containing the binary codes assigned to each caracter
    def writeBinCodes(self, alphabet, binTable, fileName):
        with open(fileName[:4]+'_BinCodes.txt','a') as f:
            for i in alphabet:
                f.write("The binary code of " + i + " is : " + str(binTable[i]) + '\n')
            f.close()



