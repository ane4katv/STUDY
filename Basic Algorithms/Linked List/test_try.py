# class Node:


class Trie:
    def __init__(self):
        self.root = {"*": "*"}

    def add_word(self, word):
        cur_node = self.root
        for letter in word:
            if letter not in cur_node:
                cur_node[letter] = {}
            cur_node = cur_node[letter]

        cur_node["*"] = "*"

    def does_word_exists(self, word):
        cur_node = self.root
        for letter in word:
            if letter not in cur_node:
                return False
            cur_node = cur_node[letter]
        return "*" in cur_node

trie = Trie()
words = ["wait", "waiter", "shop", "shopper"]
for word in words:
    trie.add_word(word)




print(trie.does_word_exists("wait"))
print(trie.does_word_exists(""))
print(trie.does_word_exists("waite"))
print(trie.does_word_exists("shop"))
print(trie.does_word_exists("shopp"))