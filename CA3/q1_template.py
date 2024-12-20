import sys
import re


INVALID_INDEX = 'invalid index'
OUT_OF_RANGE_INDEX = 'out of range index'
EMPTY = 'empty'


class MinHeap:
    class Node:
        pass

    def __init__(self):
        pass

    def bubble_up(self, index):
        pass

    def bubble_down(self, index):
        pass

    def heap_push(self, value):
        pass

    def heap_pop(self):
        pass

    def find_min_child(self, index):
        pass

    def heapify(self, *args):
        pass


class HuffmanTree:
    class Node:
        pass

    def __init__(self):
        pass

    def set_letters(self, *args):
        pass

    def set_repetitions(self, *args):
        pass

    def set_text(self, text):
        pass

    def build_tree(self):
        pass

    def get_compressed_length(self):
        pass


class Bst:
    class Node:
        pass

    def __init__(self):
        pass

    def insert(self, key):
        pass

    def preorder(self):
        pass

    def inorder(self):
        pass

    def postorder(self):
        pass


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
