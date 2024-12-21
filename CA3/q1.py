import sys
import re


INVALID_INDEX = 'invalid index'
OUT_OF_RANGE_INDEX = 'out of range index'
EMPTY = 'empty'


class MinHeap:

    def __init__(self):
        self.nodes = []

    def bubble_up(self, index):
        if not isinstance(index, int):
            raise Exception(INVALID_INDEX)
        if index < 0 or index >= len(self.nodes):
            raise Exception(OUT_OF_RANGE_INDEX)
        while index > 0:
            parent = (index - 1) // 2
            if self.nodes[index] < self.nodes[parent]:
                self.nodes[index], self.nodes[parent] = self.nodes[parent], self.nodes[index]
                index = parent
            else:
                break

    def bubble_down(self, index):
        if not isinstance(index, int):
            raise Exception(INVALID_INDEX)
        if index < 0 or index >= len(self.nodes):
            raise Exception(OUT_OF_RANGE_INDEX)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index
            if left < len(self.nodes) and self.nodes[left] < self.nodes[smallest]:
                smallest = left
            if right < len(self.nodes) and self.nodes[right] < self.nodes[smallest]:
                smallest = right
            if smallest == index:
                break
            self.nodes[index], self.nodes[smallest] = self.nodes[smallest], self.nodes[index]
            index = smallest

    def heap_push(self, value):
        self.nodes.append(value)
        self.bubble_up(len(self.nodes) - 1)

    def heap_pop(self):
        if not self.nodes:
            raise Exception(EMPTY)
        root = self.nodes[0]
        self.nodes[0] = self.nodes[-1]
        self.nodes.pop()
        if self.nodes:
            self.bubble_down(0)
        return root

    def find_min_child(self, index):
        if not isinstance(index, int):
            raise Exception(INVALID_INDEX)
        if index < 0 or index >= len(self.nodes):
            raise Exception(OUT_OF_RANGE_INDEX)
        left = 2 * index + 1
        right = 2 * index + 2
        if left >= len(self.nodes):
            return None
        if right >= len(self.nodes):
            return left
        return left if self.nodes[left] < self.nodes[right] else right

    def heapify(self, *args):
        for val in args:
            self.heap_push(val)


class HuffmanTree:
    class Node:
        def __init__(self, letter=None, freq=0, left=None, right=None):
            self.letter = letter
            self.freq = freq
            self.left = left
            self.right = right

    def __init__(self):
        self.letters = []
        self.repetitions = []
        self.root = None

    def set_letters(self, *args):
        self.letters = list(args)

    def set_repetitions(self, *args):
        self.repetitions = list(args)

    def set_text(self, text):
        freq_map = {}
        for c in text:
            freq_map[c] = freq_map.get(c, 0) + 1
        self.letters = list(freq_map.keys())
        self.repetitions = list(freq_map.values())

    def build_tree(self):
        nodes = []
        for i, letter in enumerate(self.letters):
            nodes.append(self.Node(letter, self.repetitions[i]))
        while len(nodes) > 1:
            nodes.sort(key=lambda x: x.freq)
            left = nodes.pop(0)
            right = nodes.pop(0)
            merged = self.Node(freq=left.freq + right.freq, left=left, right=right)
            nodes.append(merged)
        self.root = nodes[0] if nodes else None

    def get_compressed_length(self):
        def _dfs(node, depth):
            if not node.left and not node.right:
                return node.freq * depth
            return ((node.left and _dfs(node.left, depth + 1)) or 0) + \
                   ((node.right and _dfs(node.right, depth + 1)) or 0)

        return _dfs(self.root, 0) if self.root else 0


class Bst:
    class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = self.Node(key)
            return
        def _insert(node, val):
            if val < node.key:
                if node.left:
                    _insert(node.left, val)
                else:
                    node.left = self.Node(val)
            else:
                if node.right:
                    _insert(node.right, val)
                else:
                    node.right = self.Node(val)
        _insert(self.root, key)

    def preorder(self):
        result = []
        def _preorder(node):
            if not node:
                return
            result.append(str(node.key))
            _preorder(node.left)
            _preorder(node.right)
        _preorder(self.root)
        return ' '.join(result)

    def inorder(self):
        result = []
        def _inorder(node):
            if not node:
                return
            _inorder(node.left)
            result.append(str(node.key))
            _inorder(node.right)
        _inorder(self.root)
        return ' '.join(result)

    def postorder(self):
        result = []
        def _postorder(node):
            if not node:
                return
            _postorder(node.left)
            _postorder(node.right)
            result.append(str(node.key))
        _postorder(self.root)
        return ' '.join(result)


class Runner:
    ds_map = {'min_heap': MinHeap, 'bst': Bst, 'huffman_tree': HuffmanTree}
    call_regex = re.compile(r'^(\w+)\.(\w+)\(([\w, \-"\']*)\)$')

    def __init__(self, input_src):
        self.input = input_src
        self.items = {}

    def run(self):
        for line in self.input:
            line = line.strip()
            action, _, param = line.partition(' ')
            action_method = getattr(self, action, None)
            if action_method is None:
                return
            action_method(param)

    def make(self, params):
        item_type, item_name = params.split()
        self.items[item_name] = self.ds_map[item_type]()

    def call(self, params):
        regex_res = self.call_regex.match(params)
        item_name, func_name, args_list = regex_res.groups()

        args = [x.strip() for x in args_list.split(',')] if args_list != '' else []
        args = [x[1:-1] if x[0] in ('"', "'") else int(x) for x in args]

        method = getattr(self.items[item_name], func_name)
        try:
            result = method(*args)
        except Exception as ex:
            print(ex)
        else:
            if result is not None:
                print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
