class Node():
    def __init__(self,data,nome):
        self.nome = nome
        self.data = data
        self.next = None
        self.previous = None

    def setNext(self,next = []):
        self.next = next

