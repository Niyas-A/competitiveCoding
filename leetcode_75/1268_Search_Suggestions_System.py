class TrieNode:
    def __init__(self):
        self.children = {}
        self.products = []

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.products.append(word)
            node.products.sort()
            if len(node.products)>3:
                node.products.pop()
    
    def search(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in prefix:
            if c not in node.children:
                return []
            node = node.children[c]
        return node.products


class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        obj = Trie()
        for word in products:
            obj.insert(word)
        result = []
        for i in range(len(searchWord)):
            result.append(obj.search(searchWord[:i+1]))
        return result