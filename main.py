import xml.sax

nbElement = 0
class stack:
    __listElement = []

    def push(self,element):
        self.__listElement.insert(0,element)
        #print("Empilage de ",element)
        #print("Etat de la liste: ", self.__listElement)

    def pop(self):
       toret = self.__listElement.pop(0)
       #print("depilage de", toret)
       #print("Etat de la liste: ", self.__listElement)
       return toret

    def __init__(self):
        self.__listElement=[]
        print("Contructeur de stact")

    def isEmpty(self):
        #print("len = ", self.__listElement)
        return len(self.__listElement) == 0

    def size(self):
        return len(self.__listElement)

    def top(self):
        return  self.__listElement[0]

    def toString(self):
        print(self.__listElement)

class stackTree:
    racine : stack
    fils : []
    lefPos = 0
    rightPos = 0
    def __init__(self):
        self.racine=stack()
        self.fils=[]
        print("Contructor stack tree")

class HierachicalStack:
    stackTrees = []
    child = []


class DocElement:
    leftPos = 0
    rightPos = 0
    level = 0
    tag = ""
    value = ""

    def __init__(self, tag="", left_pos = 0, rigth_pos = 0, level = 0):
        self.leftPos = left_pos
        self.level = level
        self.rightPos = rigth_pos
        self.value = "";
        self.tag = tag

    def setTag(self,tag):
        self.tag = tag

class XMLDocument:
    element : DocElement
    childs = []

    def toString(self):
        print(self.element.value)
        for i in range(len(self.childs)):
            self.childs[i].toString();

    def posOder(self):
        toret = ""
        if self.noChilds():
            toret = toret + self.element.tag
            #print(self.element.tag)
        else:
            toret = toret + "["
            for i in range(len(self.childs)):
                self.childs[i].posOder()
                toret = toret + self.childs[i].element.tag + ","
            toret = toret + "]"
            #print(self.element.tag)
            toret = toret + self.element.tag
        print(toret)

    def preOder(self):
        toret=self.element.tag
        print(self.element.tag)
        toret = toret + "{"
        for i in range(len(self.childs)):
            self.childs[i].preOder(); ''' recursif call '''
            toret = toret + self.childs[i].element.tag +","
        toret = toret + "}"
        print(toret)

    def __init__(self, element):
        self.element = element
        self.childs = []

    def noChilds(self):
        return len(self.childs) == 0


class XMLHandler(xml.sax.ContentHandler):
    tree = ""
    doc = XMLDocument(DocElement())
    current = XMLDocument(DocElement())
    st = stack()
    index = 0
    paths = []

    def beginDocument(self):
        print("Start parsing the document")

    def startElement(self, name, attrs):
        if self.index == 0:
            self.index = 1
            self.current = XMLDocument(DocElement(name))
            self.st.push(self.current)
        else:
            self.index = 2
            x=XMLDocument(DocElement(name))
            self.st.push(self.current)
            self.current = x
        print("++++element " , name)
        self.tree = self.tree + name + "["
        if attrs :
            for (k,v) in attrs.items():
                print("attrib", k + " " + v)

    def endElement(self,name):
        print("----end element ", name)
        #x=XMLDocument()

        x=self.st.pop()
        '''
        if self.index == 1:
            print("*************list of children "+name,len(self.current.childs))
            print("ils sont : [")
            for i in range(len(self.current.childs)):
                print(self.current.childs[i].element.tag+",")
             print("]")
        '''
        if x != self.current:
            x.childs.append(self.current)

        self.current = x
        #self.tree = self.tree[0 : len(self.tree)]
        self.tree = self.tree + "], "

    '''
    def characters(self,content):
        content = content.replace("	","")
        content = content.replace("\n","")
        print("len of content :", content , " = ", len(content) )
        if len(content) > 1:
            print("====content: ",content)
            #self.tree = self.tree + content
            #self.tree = self.tree + "value:"+content
    '''
    def endDocument(self):
        print("Fin du document")
        print("tree =", self.tree)
        #print("Stack size = "+ len(stack.size()))




parser = xml.sax.make_parser()
xmlHandler = XMLHandler()
parser.setContentHandler(xmlHandler)

parser.parse(open("doc.xml","r"))
#print("After parsing ="+ xmlHandler.tree)
print("After parsing =")
xmlHandler.current.posOder()
#posorder(xmlHandler.current)



'''
fen1=Tk()
tex1= Label(fen1,text="Hello world", fg='red')
tex1.pack()
fen1.mainloop()
'''

# # # # # # # # # # # # # # # # # # # # #
#    Main Programm  for testing functions   #
# # # # # # # # # # # # # # # # # # # # #
'''
e1 = DocElement("a1")
racine = XMLDocument(e1)
d1 = XMLDocument(DocElement("b1"))
racine.childs.append(d1)
racine.childs.append(XMLDocument(DocElement("a2")))
racine.childs.append(XMLDocument(DocElement("a3")))
d1.childs.append(XMLDocument(DocElement("a4")))
d1.childs.append(XMLDocument(DocElement("b2")))
racine.childs.append(d1)
print("postOrder------------")
racine.posOder();
print("PreOdre+++++++++++++")
racine.preOder();
'''

'''
s= stack();
print(s.isEmpty())
s.push(0)
s.push(12)
s.push(13)
s.push(14)
print(s.isEmpty())
x= s.pop()
st=stackTree()
st.racine = s
st.fils.append(st)
print("type is" , type(st.fils[0]))

hs= HierachicalStack()
hs.stackTrees.append(st)
hs.child.append(hs)
'''
