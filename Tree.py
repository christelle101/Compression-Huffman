class HTree:

    def __init__(self, frequency, label, left_child = None, right_child = None):
        self.frequency = frequency
        self.label = label
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self):
        return str(self.label)
    
    #setters and getters
    def getFrequency(self):
        return self.frequency

    def getLeftChild(self):
        return self.left_child

    def getRightChild(self):
        return self.right_child

    def getLabel(self):
        return self.label

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