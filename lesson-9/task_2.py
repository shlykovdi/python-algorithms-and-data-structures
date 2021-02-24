"""
2. Закодируйте любую строку по алгоритму Хаффмана.
"""


class TreeNode:
    def __init__(self, key, value, left_child=None, right_child=None, parent=None):
        self.key = key
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent

    def has_left_child(self):
        return self.left_child is not None

    def has_right_child(self):
        return self.right_child is not None


def two_minimal_numbers_array(array):
    first_min = second_min = None
    maximum = max(array)

    for index, number in enumerate(array):
        if number <= maximum:
            maximum = number
            first_min = (number, index)

    maximum = max(array)
    for index, number in enumerate(array):
        if index != first_min[1]:
            if number <= maximum:
                maximum = number
                second_min = (number, index)

    return first_min, second_min


def create_bin_codes(main_node, bin_codes, code):
    if main_node.has_left_child():
        code += "0"
        if isinstance(main_node.left_child, str):
            bin_codes[main_node.left_child] = code
            code = code[:-1]
        else:
            create_bin_codes(main_node.left_child, bin_codes, code)
            code = code[:-1]

    if main_node.has_right_child():
        code += "1"
        if isinstance(main_node.right_child, str):
            bin_codes[main_node.right_child] = code
            code = code[:-1]
        else:
            create_bin_codes(main_node.right_child, bin_codes, code)
            code = code[:-1]


def huffman_encode(source: str) -> str:
    letters = {}
    frequency = []

    for i in source:
        if not letters.get(i):
            letters[i] = 0
        letters[i] = letters[i] + 1

    for i in letters:
        frequency.append(letters[i])

    for i in range(len(letters)-1):
        minimals = two_minimal_numbers_array(frequency)
        key_first = list(letters.keys())[minimals[0][1]]
        key_second = list(letters.keys())[minimals[1][1]]
        node_key = key_first + key_second

        frequency.remove(minimals[0][0])
        frequency.remove(minimals[1][0])
        frequency.append(minimals[0][0] + minimals[1][0])

        if len(key_first) > 1 and len(key_second) > 1:
           letters[node_key] = TreeNode(0, node_key, letters[key_first], letters[key_second])
        elif len(key_first) > 1:
           letters[node_key] = TreeNode(0, node_key, letters[key_first], key_second)
        elif len(key_second) > 1:
           letters[node_key] = TreeNode(0, node_key, key_first, letters[key_second])
        else:
           letters[node_key] = TreeNode(0, node_key, key_first, key_second)

        letters.pop(key_first)
        letters.pop(key_second)

    final_tree = letters[next(iter(letters))]

    del frequency, letters

    bin_codes = {}
    code = ""
    create_bin_codes(final_tree, bin_codes, code)

    del final_tree, code

    final_bin_string = ""
    for letter in source:
        final_bin_string += f'{bin_codes[letter]} '

    return final_bin_string


print(huffman_encode('Hello world!'))
