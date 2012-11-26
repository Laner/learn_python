class Item(object):
    def __init__(self, parent, id, text, status = "none"):
        self.parent = parent
        self.id = id
        self.text = text
        self.status = status
    
    def print_item(self):
        print self.parent, self.id, self.text, self.status
        
class Project(object):
    def __init__(self, id, text, status = "none"):
        self.id = id
        self.text = text
        self.status = status
        
    def print_item(self):
        print self.id, self.text, self.status
        
one = Item("B", "a", "Ta ut matavfallet", "none")
three = Project("A", "Regnskap", "none")
two = Project("B", "Husarbeid")
one.print_item()
two.print_item()
three.print_item()
print "----------------------------"


for one.parent in 