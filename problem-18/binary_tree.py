# Implementation of binary tree

class node:

    def __init__(self, val):
        self.val = val;
        self.l = None;
        self.r = None;

class b_tree:

    def __init__(self):
        self.root = None
    
    def get_root(self):
        return self.root

    def add(self, val):
        if (self.root is None):
            self.root = node(val)
        else:
            self._add(self, val, self.root)

    def _add(self, val, root):
        if (root.l is None):
            root.l = node(val)
        elif (root.r is None):
            root.r node(val)
        else:
            self._add(self, val, root.l)

