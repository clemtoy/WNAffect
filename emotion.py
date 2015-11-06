# -*- coding: utf-8 -*-
"""
Clement Michard (c) 2015
"""

class Emotion:
    """Defines an emotion."""
    
    emotions = {} # name to emotion (str -> Emotion)
    
    def __init__(self, name, parent_name=None):
        """Initializes an Emotion object.
            name -- name of the emotion (str)
            parent_name -- name of the parent emotion (str)
        """
        
        self.name = name
        self.parent = None
        self.level = 0
        self.children = []
        
        if parent_name:
            self.parent = Emotion.emotions[parent_name] if parent_name else None
            self.parent.children.append(self)
            self.level = self.parent.level + 1
            
            
    def get_level(self, level):
        """Returns the parent of self at the given level.
            level -- level in the hierarchy (int)        
        """
        
        em = self
        while em.level > level and em.level >= 0:
            em = em.parent
        return em
    
    
    def __str__(self):
        """Returns the emotion string formatted."""
        
        return self.name
        
        
    def nb_children(self):
        """Returns the number of children of the emotion."""
        
        return sum(child.nb_children() for child in self.children) + 1
        
        
    @staticmethod
    def printTree(emotion=None, indent="", last='updown'):
        """Prints the hierarchy of emotions.
            emotion -- root emotion (Emotion)
        """
        
        if not emotion:
            emotion = Emotion.emotions["root"]

        size_branch = {child: child.nb_children() for child in emotion.children}
        leaves = sorted(emotion.children, key=lambda emotion: emotion.nb_children())
        up, down = [], []
        if leaves:
            while sum(size_branch[e] for e in down) < sum(size_branch[e] for e in leaves):
                down.append(leaves.pop())
            up = leaves

        for leaf in up:     
            next_last = 'up' if up.index(leaf) is 0 else ''
            next_indent = '{0}{1}{2}'.format(indent, ' ' if 'up' in last else '│', " " * len(emotion.name))
            Emotion.printTree(leaf, indent=next_indent, last=next_last)
        if last == 'up':
            start_shape = '┌'
        elif last == 'down':
            start_shape = '└'
        elif last == 'updown':
            start_shape = ' '
        else:
            start_shape = '├'
        if up:
            end_shape = '┤'
        elif down:
            end_shape = '┐'
        else:
            end_shape = ''
        print('{0}{1}{2}{3}'.format(indent, start_shape, emotion.name, end_shape))
        for leaf in down:
            next_last = 'down' if down.index(leaf) is len(down) - 1 else ''
            next_indent = '{0}{1}{2}'.format(indent, ' ' if 'down' in last else '│', " " * len(emotion.name))
            Emotion.printTree(leaf, indent=next_indent, last=next_last)
