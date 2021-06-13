""" Fichier exécutable par l'utilisateur.
"""

""" Import des modules externes et internes au projet.
-   Module os : permet d'utiliser les fonctionnalités du système d'exploitation.
"""
import os
from FileProcessor import FileProcess
from BinaryProcessor import BinaryProcess
from Tree import HTree


""" La classe Encoding gère l'appel aux différentes méthodes pour le codage.
"""
class Encoding:

    """ Création d'une instance de la classe FileProcess.
    """
    file_processing = FileProcess()

    """ Création de variables:
    -   file_name : utilise input pour permettre à l'utilisateur de rentrer le nom de son fichier
    -   alphabet_and_frequency : alphabet et fréquence du fichier
    -   frequencies_list : liste des fréquences
    -   alphabet_list : liste contenant l'alphabet
    -   alphabet_freq_dic : dictionnaire avec l'alphabet et les fréquences
    -   freqThenASCIIDic : dictionnaire trié par fréquence et ASCII
    -   alphabet_size : taille de l'alphabet
    """
    file_name = input('Please enter your file name : \n')
    alphabet_and_frequency = file_processing.get_alpha_and_freq(file_name)
    frequencies_list = alphabet_and_frequency[1]
    alphabet_list = alphabet_and_frequency[0]
    alphabet = alphabet_list
    alphabet_freq_dic = file_processing.dictionary(frequencies_list, alphabet_list)
    freq_ascii_dic = file_processing.freq_then_ascii_sort(alphabet_freq_dic)
    alphabet_size = len(alphabet_list)
    frequencies_list = []
    alphabet_list = []

    """ Écriture du fichier contenant les fréquences.
    """
    file_processing.write_freq_in_file("\n The alphabet size is :    " + " " + str(alphabet_size), None, file_name)
    for pair in freq_ascii_dic:
        file_processing.write_freq_in_file(pair[0], pair[1], file_name)
        frequencies_list.append(pair[1])
        alphabet_list.append(pair[0])

    """ Gestion de l'arbre de Huffman.
    """
    tree_list = []
    for i in range(0, len(frequencies_list)):
        tree_list.append(HTree(frequencies_list[i], alphabet_list[i]))

    while (len(tree_list) > 1):
        m1 = min(tree_list)
        tree_list.remove(m1)
        m2 = min(tree_list)
        tree_list.remove(m2)
        tree_list.append(HTree(m1.frequency + m2.frequency, "", m1, m2))

    """ La racine de l'arbre est le premier élément de tree_list.
    """
    root = tree_list[0]

    bin_table = root.browse()

    """ Création d'une instance de la BinaryProcess.
    """
    bin_convert = BinaryProcess()

    """ Écriture du fichier avec les codes binaires.
    """
    bin_convert.write_bin_codes(alphabet, bin_table, file_name)

    """ Accession au contenu du fichier 
    """
    content = file_processing.get_file_content(file_name)

    """ Processus de traitement binaire.
    -   bin_list : liste des codes binaires
    -   Complétion du code binaire
    -   Écriture du fichier binaire
    """
    bin_list = bin_convert.bin_convert(content, bin_table)
    bin_convert.complete_bin_code(bin_list)
    bin_list_octet = bin_convert.create_bin_list(bin_list)
    bin_convert.write_bin_file(file_name[:4] + '_compressed.bin', bin_list_octet)

    """ Calcul du taux de compression.
    -   initial_file_size : taille initiale du fichier
    -   final_file_size : taille finale du fichier
    -   compression_rate : taux de compression = 1 - taille finale/taille initiale
    -   path() : méthode d'accession au chemin
    """
    initial_file_size = (os.path.getsize(file_name[:4] + '_compressed.bin'))
    final_file_size = (os.path.getsize(file_name))
    compression_rate = 1 - (initial_file_size/final_file_size)
    print("\n The compression rate for " + file_name + " is " + str(round(compression_rate, 2)*100) + "%")

    """ Calcul du nombre moyen de bits de stockage.
    - round() : permet d'arrondir un float
    """
    total = 0
    for i in range(0, len(alphabet_list)):
        total = total + len(bin_table[alphabet_list[i]])*frequencies_list[i]
    avgBits = round(total/sum(frequencies_list), 2)
    print("\n The average number of storage bits for one file caracter " + file_name + " " + " is : " + " " + str(avgBits))

