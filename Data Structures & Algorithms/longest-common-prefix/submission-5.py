class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Tier()

        for word in strs:
            trie.add_word(word)

        return trie.get_common_prefix()


class TierNode:
    def __init__(self):
        self.node = {}


class Tier:
    def __init__(self):
        self.root = TierNode()

    def add_word(self, word):
        node_obj = self.root

        for char in word:
            if char not in node_obj.node:
                node_obj.node[char] = TierNode()

            node_obj = node_obj.node[char]

        node_obj.node["*"] = True

    def get_common_prefix(self):
        node_obj = self.root
        prefix = ""

        while len(node_obj.node) == 1 and "*" not in node_obj.node:
            char = next(iter(node_obj.node))
            prefix += char
            node_obj = node_obj.node[char]

        return prefix