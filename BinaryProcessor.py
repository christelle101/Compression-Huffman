""" Effectue le traitement binaire du fichier.
"""
class BinaryProcess:

    """ Convertit en code binaire.
    """
    def bin_convert(self, content, bin_table):
        bin_content = ""
        for i in content:
            bin_content = bin_content + bin_table[i]
        return bin_content

    """ Complète le code binaire avec les bits manquants.
    Lorsque le code est insuffisant pour faire un octet, rajoute 0.
    """
    def complete_bin_code(self, content):
        while len(content)%8 != 0:
            content = content + "0"

    """ Retourne une liste de codes binaires associée aux caractères
    """
    def create_bin_list(self, content):
        bin_list = []
        for i in range (8, len(content), 8):
            bin_list.append(content[i-8:i])
        return bin_list

    """ Crée un fichier binaire dans le répertoire du projet.
    Fonctions utilisées :
    -   open() : ouvre file_name et retourne un objet fichier correspondant
    - write() : écrit les données
    Le paramètre "wb" indique que le fichier est ouvert pour une écriture en mode binaire.
    """
    def write_bin_file(self, file_name, content):
        with open(file_name, "wb") as opened:
            for i in content:
                opened.write((int(i, base=2)).to_bytes((len(i)//8), byteorder='big'))
        opened.close()

    """ Crée un fichier au format txt qui contient les codes binaires associés aux caractères.
    Fonctions utilisées :
    -   open() : ouvre file_name et donne un fichier correspondant
    -   close() : ferme le fichier ouvert
    Ouverture en mode 'a' : mode append pour l'addition de données, crée le fichier si il n'existe pas.
    """
    def write_bin_codes(self, alphabet, bin_table, file_name):
        with open(file_name[:4]+'_BinCodes.txt','a') as opened:
            for i in alphabet:
                opened.write("The binary code of " + i + " is : " + str(bin_table[i]) + '\n')
            opened.close()
