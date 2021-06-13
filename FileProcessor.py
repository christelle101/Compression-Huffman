""" Procède au traitement du fichier initial.
"""
class FileProcess:

    """Retourne le contenu d'un fichier dont le nom est en parametre.
    Fonctions utilisées:
        - open() : ouvre file_path et donne un objet fichier correspondant
        - read() : renvoie le nombre d'octets associés au fichier
    """
    def get_file_content(self, file_path):
        return open(file_path).read()

    """Renvoie tous les caracteres du fichier couples a leur code ASCII.
    Fonctions utilisées :
        - ord() : renvoie l'entier representant l'Unicode du caractere
    """
    def ascii_extractor(self, file_path):
        file_content = self.get_file_content(file_path)
        for c in file_content:
            print(c, ord(c))

    """Retourne l'alphabet associe au texte ainsi que la frequence de chaque caractere.
    """
    def get_alpha_and_freq(self, file_path):
        file_content = self.get_file_content(file_path)
        alphabet = []
        frequency = []
        for i in range(0, len(file_content)):
            if file_content[i] not in alphabet:
                alphabet.append(file_content[i])
                frequency.append(1)
            else:
                position = alphabet.index(file_content[i])
                frequency[position] = frequency[position] + 1
        return alphabet, frequency

    """Prend en parametre l'alphabet et la frequence et retourne un dictionnaire dic.
    Fonctions utilisées :
    -   dict() : crée un dictionnaire
    """
    def dictionary(self, alphabet, frequency):
        dic = dict()
        for k in range(0, len(alphabet)):
            dic[frequency[k]] = alphabet[k]
        return dic

    """Effectue un tri du dictionnaire passé en paramètre.
    Le tri est d'abord réalisé par fréquence puis par code ASCII.
    Fonctions utilisées :
    -   sorted() : renvoie une liste triée
    """
    def freq_then_ascii_sort(self, dic):
        return sorted(dic.items(), key = lambda x: (x[1],x[0]))

    """Crée un nouveau fichier txt qui se terminera par _Frequency.
    Fonctions utilisées :
    -   open() : ouvre file_name et donne un fichier correspondant
    -   close() : ferme le fichier ouvert
    """
    #creates a new txt file that contains each caracter and its frequency
    def write_freq_in_file(self, caracter, freq, file_name):
        with open(file_name[:4] + '_Frequency.txt', 'a') as f:
            if freq != None:
                f.write(caracter + '' + str(freq) + '\n')
            else:
                f.write(caracter + '\n')
        f.close()
