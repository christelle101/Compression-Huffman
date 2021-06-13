""" Classe qui gère l'arbre binaire de Huffman.
"""
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

    """Retourne la fréquence d'apparition.
    """
    def get_frequency(self):
        return self.frequency

    """ Retourne le fils gauche.
    """
    def get_left_child(self):
        return self.left_child

    """ Retourne le fils droit.
    """
    def get_right_child(self):
        return self.right_child

    """ Retourne le label.
    """
    def get_label(self):
        return self.label

    """ Permet de modifier la valeur de l'élément fréquence.
    [UPDATE] : inutile car on n'aura jamais besoin de modifier la fréquence.
    """
    def set_frequency(self, frequency):
        self.frequency = frequency

    """ Permet de redéfinir le champ d'action de l'opérateur >.
    Fonctions utilisées :
    -   isinstance() : retourne vrai si l'objet spécifié est de type spécifié.
    Dans ce cas, elle retourne True si other est de type HTree.
    """
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
    def get_children(self):
        children = []
        if self.right_child is not None :
            children.append(self.right_child)
        if self.left_child is not None :
            children.append(self.left_child)
        return children

    """ Gère le parcours en profondeur de l'arbre binaire de Huffman.
    """
    def browse(self, path = None, nodes={}):
        if self.get_left_child() is None and self.get_right_child() is None:
            nodes[self.label] = path
        if not self.get_left_child() is None:
            if path is None:
                self.get_left_child().browse('0')
            else:
                self.get_left_child().browse(path + '0')
        if not self.get_right_child() is None:
            if path is None:
                self.get_right_child().browse('1')
            else:
                self.get_right_child().browse(path + '1')
        return nodes

    """ Permet à l'utilisateur de dessiner l'arbre binaire de Huffman.
    """
    def draw_tree(self):
        print("Tree : -", self.label)
        self.get_children()
        if not self.get_left_child() is None:
            self.left_child.draw_tree()
        if not self.get_right_child() is None:
            self.right_child.draw_tree()
