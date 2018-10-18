class Node():
    # Attributes
    __poids = None
    __data = ""
    __childs = []

    # Initialisation
    def __init__(self, nPoids, nNodeValue, nChilds):
        __poids = nPoids
        __data = nNodeValue
        __childs = nChilds

    def setPoids(self, nPoids):
        __poids = nPoids

    def setNodeValue(self, nNodeValue):
        __data = nNodeValue

    def setChilds(self, nChilds):
        __childs = nChilds

    def getPoids(self):
        return __poids

    def getNodeValue(self):
        return __data

    def getChilds(self):
        return __childs

    def __repr__(self):
        print(__poids, __data)
        print([x.getPoids() for x in __childs])

    def __str__(self):
        text = ""
        text = "Poids : " + __poids + "\n"
        text = text + "Data : " + __data + "\n"
        text = "Childs : " + [x.getPoids() for x in __childs]
        return text


if __main__ == __name__:
    print("This should be used with algo2_2018.py")
