#from FileProcessor import FileProcess
class HTree:

    """Constructeur de la classe HTree.
    - frequency : float
    - label : str
    - left_child : noeud
    - right_child : noeud
    """
    def __init__(self, frequency, label, left_child = None, right_child = None):
        self.frequency = frequency
        self.label = label
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self):
        return "label : " + self.label + "frequency: " + str(self.frequency) + "left child: " + str(self.left_child.frequency) + "right child:" + str(self.right_child.frequency)

    """ Getters et setters.
    Fonctions qui permettent la modification et l'accession de certains attributs de l'objet.
    """
    #setters and getters

    """Retourne la fréquence d'apparition.
    """
    def getFrequency(self):
        return self.frequency

    """ Retourne le fils gauche.
    """
    def getLeftChild(self):
        return self.left_child

    """ Retourne le fils droit.
    """
    def getRightChild(self):
        return self.right_child

    """ Retourne le label.
    """
    def getLabel(self):
        return self.label

    """ Permet de modifier la valeur de l'élément fréquence.
    [UPDATE] : inutile car on n'aura jamais besoin de modifier la fréquence.
    """
    def setFrequency(self, frequency):
        self.frequency = frequency

    """ Permet de redéfinir le champ d'action de l'opérateur >.
    Fonctions utilisées :
    -   isinstance() : retourne vrai si l'objet spécifié est de type spécifié.
    Dans ce cas, elle retourne True si other est de type HTree.
    """
    #redefines the > operator
    def __gt__(self, other):
        if isinstance(other, HTree):
            if self.frequency > other.frequency:
                return True
            elif self.frequency <= other.frequency:
                return False

    """ Permet de redéfinir le champ d'action de l'opérateur <.
    Fonctions utilisées :
    -   isinstance() : retourne vrai si l'objet spécifié est de type spécifié.
    Dans ce cas, elle retourne True si other est de type HTree.
    """
    #redefines the < operator
    def __lt__(self, other):
       if isinstance(other, HTree):
           if self.frequency < other.frequency:
               return True
           elif self.frequency >= other.frequency:
               return False

    """ Crée une liste vide et y ajoute les noeuds fils.
    Fonctions utilisées :
    -   append() : ajoute un élément à la fin de la liste children
    """
    #returns the list of a node's children
    def getChildren(self):
        children = []
        if self.right_child != None :
            children.append(self.right_child)
        if self.left_child != None :
            children.append(self.left_child)
        return children

    """ Gère le parcours en profondeur de l'arbre binaire de Huffman.
    """
    #allows the user to browse the binary tree
    def browse(self, path = None, nodes={}):
        #returns the dictionary that contains the labels and their associated binary code (called path)
        if self.getLeftChild() is None and self.getRightChild() is None:
            nodes[self.label] = path
        if not self.getLeftChild() is None:
            if path is None:
                self.getLeftChild().browse('0')
            else:
                self.getLeftChild().browse(path + '0')
        if not self.getRightChild() is None:
            if path is None:
                self.getRightChild().browse('1')
            else:
                self.getRightChild().browse(path + '1')
        return nodes

    """ Permet à l'utilisateur de dessiner l'arbre binaire de Huffman.
    """
    #prints the binary tree
    def drawTree(self):
        print("Tree : -", self.label)
        self.getChildren()
        if not self.getLeftChild() is None:
            self.left_child.drawTree()
        if not self.getRightChild() is None:
            self.right_child.drawTree()
