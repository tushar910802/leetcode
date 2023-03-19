class WordDictionary:
    def __init__(self):
        self.root = {}
    
    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['$'] = True
    
    def search(self, word: str) -> bool:
        return self.searchHelper(word, self.root)
    
    def searchHelper(self, word: str, node: dict) -> bool:
        if not word:
            return '$' in node
        c = word[0]
        if c == '.':
            for child in node.values():
                if self.searchHelper(word[1:], child):
                    return True
            return False
        if c not in node:
            return False
        return self.searchHelper(word[1:], node[c])


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)