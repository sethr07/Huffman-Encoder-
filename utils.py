from inspect import Attribute


class Node:
    """_summary_
    Tree Node for HF Tree
    """
    def __init__(self, symbol, prob, left = None, right = None):
        self.symbol = symbol
        self.prob = prob
        self.left = left
        self.right = right 
        self.code = ''

codes = dict()

def entropy_gain (data, coding, symbols, freq):
    """
    Calculates Entropy between inital str and encoded output. Gives information about the compreession

    Args:
        data (Initial String): String by user
        coding (dict): HF Encoded for each char
        symbols (str): chars in str
        freq (_type_): Counter of chars in str
    """
    bc, ac = len(data) * 8, 0

    for s in symbols:
        count = freq[s]
        ac += count * len(coding[s])

    #print("\n")
    #print("-------------------------------------------------")
    #print("-------------------------------------------------")
    #print("Entropy before Compression (bits): ", bc)
    #print("Entropy after Compression (bits): ", ac)
    #print("-------------------------------------------------")
    #print("-------------------------------------------------")
    return bc, ac


def count_elements(data) -> dict():
    """_summary_
    Counts the number of elements 

    Args:
        data (str): Inital string by user

    Returns:
        dict:  returns a dict with char:count
    """
    freq = {}

    for i in range(len(data)):
        if data[i] in freq:
            freq[data[i]] += 1
        else:
            freq[data[i]] = 1
    
    freq = dict(sorted(freq.items(), key=lambda item: item[1]))
    return freq


def calculate_code(node, val ="") -> dict():
    """_summary_
    Read the tree from top to bottom and the find the char to add the the HF codes
    Args:
        node (Node): Node of tree
        val (str): To calculaate the HF code when traversing. Defaults to "".

    Returns:
        dict: HF encoded each char
    """
    newVal = val + str(node.code)

    if node.left:
        calculate_code(node.left, newVal)
    if node.right:
        calculate_code(node.right, newVal)
    if not node.left and not node.right:
        #print(f"{node.symbol} -> {newVal}")
        codes[node.symbol] = newVal
    
    return codes

def encode_it(data, coding) -> str:
    """
    Encoded given str
    Args:
        data (str): init string
        coding (dict): encoded char in str HF

    Returns:
        str: Encoded str
    """

    out = []

    for c in data:
        out.append(coding[c])
    
    out_str = "".join([str(item) for item in out])
    return out_str

def huffman(freq, ini_str):
    symbols = freq.keys()
    probabilites = freq.values()
    
    nodes = []

    for s, p in zip(symbols, probabilites):
        n = Node(s, p)
        nodes.append(n)
    
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x:x.prob)

        right = nodes[0]
        left = nodes[1]
        left.code = 0
        right.code = 1

        newnode = Node(left.symbol + right.symbol, left.prob + right.prob, left, right)
        
        nodes.remove(right)
        nodes.remove(left)
        nodes.append(newnode)

    hf = calculate_code(nodes[0])
    ec = encode_it(ini_str, hf)
    bsize, asize = entropy_gain(ini_str, hf,symbols, freq)
    
    return ec, bsize, asize, nodes[0]


def decode_HF(encoded, huffman_tree) -> str:

    tree_head = huffman_tree
    decoded = []

    for s in encoded:
        if s == '1':
            huffman_tree = huffman_tree.right 
        elif s == '0':
            huffman_tree = huffman_tree.left
        
        try:
            if huffman_tree.left.symbol == None and huffman_tree.right.symbol == None:
                pass
        except AttributeError:
            decoded.append(huffman_tree.symbol)
            huffman_tree = tree_head
    
    res = "".join([str(item) for item in decoded])
    return res

    


