""" Calcule le nombre moyen de bits de stockage.
"""
class AverageStorageBits:

    """ Constructeur de la classe AverageStorageBits.
    -   binAlphabet : alphabet binaire
    -   frequencies : fréquences d'apparition
    -   initialFile : fichier initial
    """
    def __init__(self, bin_alphabet: dict, frequencies: dict, initial_file:str):
        self.bin_alphabet = bin_alphabet
        self.frequencies = frequencies
        self.initial_file = initial_file

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

    """ Retourne le nombre moyen de bits de stockage.
    """
    def calculate_avg_storage(self):
        total = 0
        bin_tree = self.get_bin_alphabet()
        for caracter in bin_tree.values():
            total += len(caracter)
        return total/len(bin_tree)
