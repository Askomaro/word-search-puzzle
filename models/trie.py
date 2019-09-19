# Take my own realization of compact prefix tree -> https://github.com/Askomaro/python_trie


class Node(object):
    def __init__(self, is_end=False):
        self.children = {}
        self.label = {}
        self.is_full_word = is_end


class Trie(object):
    def __init__(self):
        self.root = Node()

    def insert(self, word: str):
        """
        Inserts a word into a trie
        :type word: str
        :rtype: void
        """
        current_node = self.root
        i = 0

        while i < len(word) and word[i] in current_node.label:
            j = 0
            index = word[i]
            label = current_node.label[index]

            while j < len(label) and i < len(word) and label[j] == word[i]:
                i += 1
                j += 1

            if j == len(label):
                current_node = current_node.children[index]
            else:
                if i == len(word):
                    ex_child = current_node.children[index]
                    new_child = Node(True)
                    remaining_label = label[j:]

                    current_node.label[index] = label[:j]
                    current_node.children[index] = new_child
                    new_child.children[remaining_label[0]] = ex_child
                    new_child.label[remaining_label[0]] = remaining_label
                else:
                    remaining_label = label[j:]
                    remaining_word = word[i:]

                    new_child = Node()
                    ex_child = current_node.children[index]

                    current_node.label[index] = label[:j]
                    current_node.children[index] = new_child

                    new_child.children[remaining_label[0]] = ex_child
                    new_child.label[remaining_label[0]] = remaining_label
                    new_child.label[remaining_word[0]] = remaining_word
                    new_child.children[remaining_word[0]] = Node(True)

                return

        if i < len(word):
            current_node.label[word[i]] = word[i:]
            current_node.children[word[i]] = Node(True)
        else:
            current_node.is_full_word = True

    def insert_list(self, words: [str]):
        """
        Inserts a word into a trie
        :type words: list of str
        :rtype: void
        """
        for word in words:
            self.insert(word)

    def find(self, word) -> bool:
        """
        Returns True if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        i = 0
        current_node = self.root

        while i < len(word) and word[i] in current_node.label:
            j = 0
            index = word[i]
            label = current_node.label[index]

            while j < len(label) and i < len(word):
                if word[i] != label[j]:
                    return False
                i += 1
                j += 1

            if j == len(label) and len(word) >= i:
                current_node = current_node.children[index]
            else:
                return False

        return i == len(word) and current_node.is_full_word
