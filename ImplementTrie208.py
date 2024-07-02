class Trie(object):

    def __init__(self):
        self.container = {}

        # {r: {a: {m: {i: {}} }, u: {n: {n: {i} }} }, a: {d: {a: {m: {}}}} }

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.container
        for char in word:
            if char in cur:
                cur = cur[char]
            else:
                cur[char] = {}
                cur = cur[char]
        cur["END"] = None

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cur = self.container
        for char in word:
            if char in cur:
                cur = cur[char]
            else:
                return False
            
        if "END" in cur:
            return True
        return False

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        cur = self.container
        for char in prefix:
            if char in cur:
                cur = cur[char]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("rami")
obj.insert("randy")
print(obj.container)
print(obj.startsWith("rao"))
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)