class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        strs = sorted(strs)

        trie = Tier()

        for word in strs:
            trie.add_word(word)
        
        common_prefix = trie.get_common_prefix()

        return common_prefix


class TierNode:

    def __init__(self) -> None:
        self.node = {}

class Tier:

    def __init__(self):
        self.root = TierNode()
    
    def add_word(self, word):

        node = self.root

        for char in word:
            if char in node.node:
                node = node.node[char]
            else:
                new_node = TierNode()
                node.node[char] = new_node
                node = new_node
        
        node.node["*"] = True

    def get_sub_nodes(self, node):
        keys = node.keys()
        sub_nodes = [node[key].node for key in keys]

        return sub_nodes
    
    def get_common_prefix(self):

        root_node = self.root.node
        common_prefix = ""

        if len(root_node) == 0 or len(root_node) >1:
            return common_prefix
        else:
            sub_nodes = [root_node]
            while len(sub_nodes) == 1:

                sub_node_keys = list(sub_nodes[0].keys())
                
                if len(sub_node_keys) > 1 or "*" in sub_node_keys:
                    break

                common_prefix += sub_node_keys[0]
                sub_nodes = self.get_sub_nodes(sub_nodes[0])
        
        return common_prefix

