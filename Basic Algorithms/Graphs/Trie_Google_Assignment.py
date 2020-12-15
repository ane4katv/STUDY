# https://youtu.be/hjUJFjcrbR4?t=798


class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode("*")

    def insert(self, word):
        cur_node = self.root

        for letter in word:
            if letter not in cur_node.children:
                cur_node.children[letter] = TrieNode(letter)

            cur_node = cur_node.children[letter]

        cur_node.end = True

    def search(self, word):
        if word == "":
            return True
        cur_node = self.root
        for letter in word:
            if letter not in cur_node.children:
                return False
            cur_node = cur_node.children[letter]
        return cur_node.end

    def starts_with(self, prefix):
        cur_node = self.root
        for letter in prefix:
            if letter not in cur_node.children:
                return False
            cur_node = cur_node.children[letter]
        return True


trie = Trie()

trie.insert("apple")
print(trie.search("apple"))   # returns true
print(trie.search("app"))    # returns false
print(trie.starts_with("app")) # returns true
trie.insert("app")
print(trie.search("app"))     # returns true

"""
From original Google assignment

Implement a trie with insert, search, and startsWith methods.
Example:

trie = new Trie()

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true

word: M
N of word
Space complexity O(NM)
Search operation is O(NM)
====>
Space: O(M)
Search: O(M)

list[1] = word
list[2] = words2
26

list
M layers
layers: a b c d e f ….. z =>26
layers: a b c d e f ….. z =>26
layers: a b c d e f ….. z =>26
layers: a b c d e f ….. z =>26
"""

