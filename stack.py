class stack:
    listElement = []

    def push(self,element):
        self.listElement.insert(0,element);

    def pop(self):
        self.listElement.pop(0)

    def __init__(self):
        self.listElement=[]
        print("Contructeur de stact")