""" Permet de calculer le taux de compression.
"""
class CompressionRate:

    """ Constructeur de la classe compression_rate.
    -   binAlphabet : alphabet binaire
    -   frequencies : fréquences
    -   initialFile : fichier initial
    -   savedRatio : taux d'espace gagné
    """
    def __init__(self, bin_alphabet: dict, frequencies: dict, initial_file:str):
        self.bin_alphabet = bin_alphabet
        self.frequencies = frequencies
        self.initial_file = initial_file
        self.saved_ratio = self.calculate_ratio()

    """ Getters et setters.
    Fonctions qui permettent la modification et l'accession de certains attributs de l'objet.
    """

    """ Retourne l'alphabet binaire.
    """
    def get_bin_alphabet(self):
        return self.bin_alphabet

    """ Retourne les fréquences d'apparition.
    """
    def get_frequencies(self):
        return self.frequencies

    """ Retourne le fichier initial.
    """
    def get_initial_file(self):
        return self.initial_file

    """ Retourne le taux de données gagnées.
    """
    def get_saved_ratio(self):
        return self.saved_ratio

    """ Retourne le taux de compression personnalisé pour un fichier donné
    """
    def calculate_ratio(self):
        compresion_count = 0
        initial_count = len(self.get_initial_file())*8

        for caracter in self.get_frequencies():
            compresion_count += int(len(self.get_bin_alphabet()[caracter[0]] * caracter[1]))
        print(compresion_count, initial_count)
        return 1 - float(compresion_count/initial_count)
