""" Fichier exécutable par l'utilisateur.
"""

""" Import des modules externes et internes au projet.
-   Module os : permet d'utiliser les fonctionnalités du système d'exploitation.
"""

#class imports
import os
from FileProcessor import FileProcess
from BinaryProcessor import BinaryProcess
from Tree import HTree
#from AvgBits import AverageStorageBits
#from CompressionRate import CompressionRate

""" La classe Encoding gère l'appel aux différentes méthodes pour le codage.
"""
class Encoding:

    """ Création d'une instance de la classe FileProcess.
    """
    fileProcessing = FileProcess()

    """ Création de variables:
    -   fileName : utilise input pour permettre à l'utilisateur de rentrer le nom de son fichier
    -   alphabetAndFrequency : alphabet et fréquence du fichier
    -   frequenciesList : liste des fréquences
    -   alphabetList : liste contenant l'alphabet
    -   alphabetFreqDic : dictionnaire avec l'alphabet et les fréquences
    -   freqThenASCIIDic : dictionnaire trié par fréquence et ASCII
    -   alphabetSize : taille de l'alphabet
    """
    fileName = input('Please enter your file name : \n')
    alphabetAndFrequency = fileProcessing.getAlphabetandFreq(fileName)
    frequenciesList = alphabetAndFrequency[1]
    alphabetList = alphabetAndFrequency[0]
    alphabet = alphabetList
    alphabetFreqDic = fileProcessing.dictionary(frequenciesList, alphabetList)
    freqASCIIdic = fileProcessing.freqThenASCII_sort(alphabetFreqDic)
    alphabetSize = len(alphabetList)
    frequenciesList = []
    alphabetList = []

    """ Écriture du fichier contenant les fréquences.
    """
    fileProcessing.writeFreqInFile("\n The alphabet size is :    " + " " + str(alphabetSize), None, fileName)
    for pair in freqASCIIdic:
        fileProcessing.writeFreqInFile(pair[0], pair[1], fileName)
        frequenciesList.append(pair[1])
        alphabetList.append(pair[0])

    """ Gestion de l'arbre de Huffman.
    """
    treeList = []
    for i in range(0, len(frequenciesList)):
        treeList.append(HTree(frequenciesList[i], alphabetList[i]))

    while (len(treeList) > 1):
        m1 = min(treeList)
        treeList.remove(m1)
        m2 = min(treeList)
        treeList.remove(m2)
        treeList.append(HTree(m1.frequency + m2.frequency, "", m1, m2))

    """ La racine de l'arbre est le premier élément de treeList.
    """
    root = treeList[0]

    binTable = root.browse()

    """ Création d'une instance de la BinaryProcess.
    """
    binConvert = BinaryProcess()

    """ Écriture du fichier avec les codes binaires.
    """
    binConvert.writeBinCodes(alphabet, binTable, fileName)

    """ Accession au contenu du fichier 
    """
    content = fileProcessing.getFileContent(fileName)

    """ Processus de traitement binaire.
    -   binList : liste des codes binaires
    -   Complétion du code binaire
    -   Écriture du fichier binaire
    """
    binList = binConvert.BinConvert(content, binTable)
    binConvert.completeBinCode(binList)
    binListOctet = binConvert.createBinList(binList)
    binConvert.writeBinFile(fileName[:4] + '_compressed.bin', binListOctet)

    """ Calcul du taux de compression.
    -   initialFileSize : taille initiale du fichier
    -   finalFileSize : taille finale du fichier
    -   compressionRate : taux de compression = 1 - taille finale/taille initiale
    -   path() : méthode d'accession au chemin
    """
    initialFileSize = (os.path.getsize(fileName[:4] + '_compressed.bin'))
    finalFileSize = (os.path.getsize(fileName))
    compressionRate = 1 - (initialFileSize/finalFileSize)
    print("\n The compression rate for " + fileName + " is " + str(round(compressionRate, 2)*100) + "%")

    """ Calcul du nombre moyen de bits de stockage.
    - round() : permet d'arrondir un float
    """
    Total = 0
    for i in range(0, len(alphabetList)):
        Total = Total + len(binTable[alphabetList[i]])*frequenciesList[i]
    avgBits = round(Total/sum(frequenciesList), 2)
    print("\n The average number of storage bits for one file caracter " + fileName + " " + " is : " + " " + str(avgBits))

