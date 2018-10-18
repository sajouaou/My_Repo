"""
__author__ = Antunes Coimbra André,Ajouaou Soufiane
__version__ = 1.0
__date__ = 18/10/2018
"""


class Node():
    # Attributes
    __poids = None
    __data = ""
    __childs = []

    def __init__(self, nPoids, nNodeData, nChilds):
        """
            # Descrption :  Initialisation of the Node
        """
        __poids = nPoids
        __data = nNodeData
        __childs = nChilds

    def setPoids(self, nPoids):
        """
            # Descrption :  Sets node weight to an newer weight
            # Params :      nPoids  -> new weight
        """
        self.__poids = nPoids

    def setNodeData(self, nNodeData):
        """
            # Descrption :  Sets node data to a newer value
            # Params :      nNodeData  -> new data
        """
        self.__data = nNodeData

    def setChilds(self, nChilds):
        """
            # Descrption :  Sets node childs list to a newer list
            # Params :      nChilds  -> new list of childs
        """
        self.__childs = nChilds

    def addChild(self, nChild):
        """
            # Descrption :  Adds a new child to the list of childs
            # Params :      nChild  -> new child node
        """
        self.__childs.append(nChild)

    def deleteChild(self, nChild):
        """
            # Descrption :  Deletes a child from the list of childs
            # Params :      nChild  -> child node which has to be deleted
        """
        self.__childs.remove(nChild)

    def getPoids(self):
        """
            # Descrption :  Gets the weight of the node
        """
        return self.__poids

    def getNodeData(self):
        """
            # Descrption :  Gets the data of the node
        """
        return self.__data

    def getChilds(self):
        """
            # Descrption :  Gets the list of children of the node
        """
        return self.__childs

    def __repr__(self):
        """
            # Descrption :  Prints the reprenetation of the node
        """
        print(__poids, __data)
        print([x.getPoids() for x in self.__childs])

    def __str__(self):
        """
            # Descrption :  Returns a string containing the information about
                            the node
        """
        text = ""
        text = text + "Data : " + self.__data + "\n"
        text = "Poids : " + self.__poids + "\n"
        text = "Childs : " + [x.getPoids() for x in self.__childs]
        return text


if __main__ == __name__:
    print("This should be used with algo2_2018.py")
