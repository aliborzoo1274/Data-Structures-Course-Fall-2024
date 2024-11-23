import sys
import re


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.empty():
            return None
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def empty(self):
        return len(self.items) == 0

    def one_line_str(self):
        return ' '.join(map(str, self.items))


class Stack:
    def __init__(self, capacity=10):
        self.max_capacity = capacity
        self.items = []

    def push(self, value):
        if len(self.items) >= self.max_capacity:
            self.expand()
        self.items.append(value)

    def pop(self):
        if self.empty():
            return None
        return self.items.pop()

    def put(self, value):
        if not self.empty():
            self.pop()
        self.push(value)

    def peek(self):
        if self.empty():
            return None
        return self.items[-1]

    def expand(self):
        self.max_capacity *= 2

    def capacity(self):
        return self.max_capacity

    def size(self):
        return len(self.items)

    def empty(self):
        return len(self.items) == 0

    def one_line_str(self):
        return ' '.join(map(str, self.items))


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_back(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def one_line_str(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return ' '.join(values)


class Runner:
    ds_map = {'stack': Stack, 'queue': Queue, 'linked_list': LinkedList}
    call_regex = re.compile(r'^(\w+)\.(\w+)\(([\w, ]*)\)$')

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
        args = args_list.split(',') if args_list != '' else []

        method = getattr(self.items[item_name], func_name)
        result = method(*args)
        if result is not None:
            print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
