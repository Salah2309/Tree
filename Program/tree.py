class Tree:
    def __init__(self, d, o=0):
        self.val = d
        self.children = []
        self.order = o
    def addChild(self, d):
        self.children.append(Tree(d, len(self.children)))
    def addChildren(self, d):
        for i in d: self.children.append(Tree(i, len(self.children)))
    def find(self, d):
        if self.val == d: return self
        for c in self.children:
            r = c.find(d)
            if r: return r
        return None
    
    def findParent(self, d):
        for c in self.children:
            if c.val == d: return self
            p = c.findParent(d)
            if p: return p
            
    def switch(self, f, s):#WIP
        f = self.find(f)
        s = self.find(s)
        if not f or not s: return False
        pf = self.findParent(f.val)
        ps = self.findParent(s.val)
        
        print(pf)
        print(ps)
        print()
        
        if pf and ps:
            t = s.order
            s.order = f.order
            f.order = t
            pf.children[pf.children.index(f)] = s
            ps.children[ps.children.index(s)] = f            
        
        print(pf)
        print(ps)
        print()
        
        return True
    
    def swap(self, f, s):
        f = self.find(f)
        s = self.find(s)
        if not f or not s: return False
        v = s.val
        s.val = f.val
        f.val = v
        return True
    
    def __repr__(self):
        return self.printTree()
    
    def printTree(self, markerStr="├── ", levelMarkers=[]):
        f = ""
        emptyStr = " "*len(markerStr)
        markers = "".join(map(lambda draw: "│" + emptyStr[:-1] if draw else emptyStr, levelMarkers[:-1]))
        markers += markerStr if len(levelMarkers) > 0 else ""
        f += f"{markers}{self.val}\n"
        for i, child in enumerate(self.children):
            isLast = i == len(self.children) - 1
            if (i == len(self.children) - 1): 
                markerStr = "└── "
            else:
                markerStr = "├── "
            f += child.printTree(markerStr, [*levelMarkers, not isLast])
        return f

head = Tree("head")
head.addChildren(["x", "y"])
head.children[0].addChildren(["a", "b", "c"])
head.children[1].addChildren(["d", "e", "f"])
z = head.find("c")
if z: z.addChild("q")


# head.printer()
# head.switch("y", "q")
# print(head)
# __repr__
# print(head.pt())

print(head)