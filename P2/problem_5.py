class TrieNode (object):
    def __init__(self):
        self.is_word = False
        self.children = {}

    def insert (self, char):
        self.children[char] = TrieNode()


    def suffixes(self, suffix=''):
    
        autocomplete_list = []
        
        for k in self.children.keys(): #.items():
            #for char in self.children.keys(): #.items():
            if self.children[k].is_word:
                autocomplete_list.append(suffix + k)
            if self.children[k].children:
                autocomplete_list.extend(self.children[k].suffixes(suffix + k))
            
        return autocomplete_list
   



class Trie (object):
    def __init__(self):
        self.root = TrieNode()


    def insert (self, word):

        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] =  TrieNode()
              
            current_node = current_node.children[char]

        current_node.is_word = True
    


    def find (self, prefix):

        current_node = self.root

        for char in prefix:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return None
        return current_node




MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')


#Test cases    
print(MyTrie.find("a").suffixes())
print(MyTrie.find("f").suffixes())
print(MyTrie.find("t").suffixes())

print(MyTrie.find("ant").suffixes())
print(MyTrie.find("fu").suffixes())
print(MyTrie.find("tri").suffixes())


print(MyTrie.find("anth").suffixes())
print(MyTrie.find("funct").suffixes())
print(MyTrie.find("").suffixes())


# ['nt', 'nthology', 'ntagonist', 'ntonym']
# ['un', 'unction', 'actory']
# ['rie', 'rigger', 'rigonometry', 'ripod']
# ['hology', 'agonist', 'onym']
# ['n', 'nction']
# ['e', 'gger', 'gonometry', 'pod']
# ['ology']
# ['ion']
# ['ant', 'anthology', 'antagonist', 'antonym', 'fun', 'function', 'factory', 'trie', 'trigger', 'trigonometry', 'tripod']


