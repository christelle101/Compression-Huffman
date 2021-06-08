#Main executable file

#class imports
import os
from FileProcessor import FileProcess
from BinaryProcessor import BinaryProcess
from Tree import HTree
#from AvgBits import AverageStorageBits
#from CompressionRate import CompressionRate

class Encoding:

    fileProcessing = FileProcess()

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

    fileProcessing.writeFreqInFile("\n The alphabet size is :    " + " " + str(alphabetSize), None, fileName)
    for pair in freqASCIIdic:
        fileProcessing.writeFreqInFile(pair[0], pair[1], fileName)
        frequenciesList.append(pair[1])
        alphabetList.append(pair[0])

    treeList = []
    for i in range(0, len(frequenciesList)):
        treeList.append(HTree(frequenciesList[i], alphabetList[i]))

    while (len(treeList) > 1):
        m1 = min(treeList)
        treeList.remove(m1)
        m2 = min(treeList)
        treeList.remove(m2)
        treeList.append(HTree(m1.frequency + m2.frequency, "", m1, m2))

    root = treeList[0]

    binTable = root.browse()

    binConvert = BinaryProcess()

    binConvert.writeBinCodes(alphabet, binTable, fileName)

    content = fileProcessing.getFileContent(fileName)

    binList = binConvert.BinConvert(content, binTable)

    binConvert.completeBinCode(binList)

    binListOctet = binConvert.createBinList(binList)

    binConvert.writeBinFile(fileName[:4] + '_compressed.bin', binListOctet)

    initialFileSize = (os.path.getsize(fileName[:4] + '_compressed.bin'))
    finalFileSize = (os.path.getsize(fileName))

    compressionRate = 1 - (initialFileSize/finalFileSize)

    print("\n The compression rate for " + fileName + " is " + str(round(compressionRate, 2)*100) + "%")

    Total = 0

    for i in range(0, len(alphabetList)):
        Total = Total + len(binTable[alphabetList[i]])*frequenciesList[i]
    
    avgBits = round(Total/sum(frequenciesList), 2)
    print("\n The average number of storage bits for one file caracter " + fileName + " " + " is : " + " " + str(avgBits))

