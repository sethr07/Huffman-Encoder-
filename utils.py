class Node:
    def __init__(self, symbol, prob, left = None, right = None):
        self.symbol = symbol
        self.prob = prob
        self.left = left
        self.right = right 
        self.code = ''

codes = dict()

def entropy_gain (data, coding, symbols, freq):
    bc, ac = len(data) * 8, 0

    for s in symbols:
        count = freq[s]
        ac += count * len(coding[s])

    print("\n")
    print("-------------------------------------------------")
    print("-------------------------------------------------")
    print("Entropy before Compression (bits): ", bc)
    print("Entropy after Compression (bits): ", ac)
    print("-------------------------------------------------")
    print("-------------------------------------------------")


def count_elements(data) -> dict():
    """_summary_
    Counts the number of elements 

    Args:
        data (_type_): _description_

    Returns:
        _type_: _description_ returns a dict with char:count
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
        node (_type_): _description_
        val (str, optional): _description_. Defaults to "".

    Returns:
        _type_: _description_
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
    out = []

    for c in data:
        out.append(coding[c])
    
    out_str = "".join([str(item) for item in out])
    return out_str

def Huffman(freq, ini_str) -> str:
    symbols = freq.keys()
    probabilites = freq.values()
    #print(symbols, probabilites)

    nodes = []

    for s in symbols:
        n = Node(s, freq.get(s))
        nodes.append(n)
    
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x:x.prob)

        right = nodes[0]
        left = nodes[1]
        left.code = 0
        right.code = 1

        newNode = Node(left.symbol + right.symbol, left.prob + right.prob, left, right)
        
        nodes.remove(right)
        nodes.remove(left)
        nodes.append(newNode)

    hf = calculate_code(nodes[0])
    ec = encode_it(ini_str, hf)
    entropy_gain(ini_str, hf,symbols, freq)
    
    return ec

    


