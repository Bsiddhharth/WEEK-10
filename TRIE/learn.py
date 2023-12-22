class trienode:
    def __init__(self):
        self.children={}    
        self.is_end_word=False
        
class trie:
    def __init__(self):
        self.root=trienode()            
      
    def insert(self,word):
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]=trienode()
            node=node.chidren[char]
        node.is_end_word=True
    
    def search(self,word) :
        node=self.root
        for char in word:
            if char not in node.children:
                return False
            node=node.children[char]
        return node.is_end_word
    
    def start_prefix(self,pre):
        node=self.root
        for char in pre:
            if char not in node.children:
                return False       
            node=node.children[char]
        return True    