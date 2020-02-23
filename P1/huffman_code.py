import sys
from collections import Counter


def compute_frequencies (data):

    data = data.replace(" ", "")
#    print(data)
    freq = Counter(data)
    freq = sorted(freq.items(), key=lambda pair: pair[1], reverse=False)
    return freq

def huffman_encoding(data):
    pass

def huffman_decoding(data,tree):
    pass

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    # print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # print ("The content of the data is: {}\n".format(a_great_sentence))

    # encoded_data, tree = huffman_encoding(a_great_sentence)

    # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # print ("The content of the encoded data is: {}\n".format(encoded_data))

    # decoded_data = huffman_decoding(encoded_data, tree)

    # print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # print ("The content of the encoded data is: {}\n".format(decoded_data))
    a = compute_frequencies(a_great_sentence)
    print(a[0][0]+a[1][0])


    # for i in a:
    #     print(i[1])