from FileProcessor import FileProcess
class HTree:

    def __init__(self, frequency, label, left_child = None, right_child = None):
        self.frequency = frequency
        self.label = label
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self):
        return "label : " + self.label + "frequency: " + str(self.frequency) + "left child: " + str(self.left_child.frequency) + "right child:" + str(self.right_child.frequency)

    #setters and getters
    def getFrequency(self):
        return self.frequency

    def getLeftChild(self):
        return self.left_child

    def getRightChild(self):
        return self.right_child

    def getLabel(self):
        return self.label

    def setFrequency(self, frequency):
        self.frequency = frequency

    #functions
    def is_leaf(self): #returns a boolean which indicates whether the node is a leaf or not
        return self.left_child is None and self.right_child is None

    #returns the list of a node's children
    def getChildren(self):
        children = []
        if self.right_child != None :
            children.append(self.right_child)
        if self.left_child != None :
            children.append(self.left_child)
        return children

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

