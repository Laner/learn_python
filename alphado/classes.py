items = []
projects = []

class Item(object):
    def __init__(self, parent, id, text, status = "none"):
        self.parent = parent
        self.id = id
        self.text = text
        self.status = status
        items.append(self)
        
    def __repr__(self):
        return str(self.text)
    
    def print_item(self):
        print self.parent, self.id, self.text, self.status
        
class Project(object):
    def __init__(self, id, text, status = "none"):
        self.id = id
        self.text = text
        self.status = status
        projects.append(self)
    
    def __repr__(self):
        return str(self.text)
        
    def print_item(self):
        print self.id, self.text, self.status
        
one = Item("B", "a", "Ta ut matavfallet", "none")
three = Project("A", "Regnskap", "none")
two = Project("B", "Husarbeid")
four = Item("B", "b", "Rydde")
one.print_item()
two.print_item()
three.print_item()
print "----------------------------"
print items

for project in projects:
    print project, ":"
    for item in items:
        if item.parent == project.id:
            print "- " + item.text
