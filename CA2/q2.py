import sys
import re


class Node:
    def __init__(self, name, line_number, children=None):
        self.name = name
        self.line_number = line_number
        self.children = {} if children is None else children

    def add_child(self, node):
        unique_entry = f'{node.name}#{node.line_number}'
        self.children[unique_entry] = node


class ProgramNode(Node):
    pass


class FunctionDeclaration(Node):
    pass


class IfStatement(Node):
    pass


class SimpleStatement(Node):
    pass


def print_result(program_node):
    from collections import deque
    queue = deque([program_node])
    condition_counter = 1
    result = []
    condition_mapping = {}

    def get_condition_name():
        nonlocal condition_counter
        condition_name = f'condition_{condition_counter}'
        condition_counter += 1
        return condition_name

    def process_conditions(conditions):
        while conditions:
            current_node = conditions.popleft()
            condition_name = condition_mapping[current_node.line_number]
            result.append(f'\ndef {condition_name}():')
            for child_key in current_node.children:
                child = current_node.children[child_key]
                if isinstance(child, IfStatement):
                    new_condition_name = get_condition_name()
                    condition_mapping[child.line_number] = new_condition_name
                    result.append(f'  {new_condition_name}()')
                    conditions.append(child)
                else:
                    result.append(f'  {child.name}')

    while queue:
        current_node = queue.popleft()

        if isinstance(current_node, ProgramNode):
            for child_key in current_node.children:
                child = current_node.children[child_key]
                queue.append(child)

        elif isinstance(current_node, FunctionDeclaration):
            result.append(f'def {current_node.name}():')
            current_conditions = deque()
            for child_key in current_node.children:
                child = current_node.children[child_key]
                if isinstance(child, IfStatement):
                    condition_name = get_condition_name()
                    condition_mapping[child.line_number] = condition_name
                    result.append(f'  {condition_name}()')
                    current_conditions.append(child)
                else:
                    result.append(f'  {child.name}')
                queue.append(child)
            process_conditions(current_conditions)

    # Print the result
    for line in result:
        print(line)




class Handler:
    def __init__(self):
        self.program = ProgramNode('program', 0)
        self.stack = []

    def function(self, name, line_number):
        new_node = FunctionDeclaration(name, line_number)
        self.program.add_child(new_node)
        self.stack.append(new_node)

    def condition(self, line_number):
        new_node = IfStatement('condition', line_number)
        self.stack[-1].add_child(new_node)
        self.stack.append(new_node)

    def statement(self, name, line_number):
        new_node = SimpleStatement(name, line_number)
        self.stack[-1].add_child(new_node)

    def endscope(self):
        self.stack.pop()


class Runner:
    func_regex = re.compile(r'^def (\w+)\(\):$')
    if_regex = re.compile(r'^if True:$')
    statement_regex = re.compile(r'^(\w+)$')
    endscope_regex = re.compile(r'^# end_scope$')

    def __init__(self, input_src):
        self.input = input_src
        self.handler = Handler()

    def run(self):
        for i, line in enumerate(self.input):
            line = line.strip()
            if not line:
                continue

            match_func = self.func_regex.match(line)
            match_if = self.if_regex.match(line)
            match_statement = self.statement_regex.match(line)
            match_endscope = self.endscope_regex.match(line)

            if match_func:
                name = match_func.group(1)
                self.handler.function(name, i)
            elif match_if:
                self.handler.condition(i)
            elif match_statement:
                name = match_statement.group(1)
                self.handler.statement(name, i)
            elif match_endscope:
                self.handler.endscope()
            else:
                print('Invalid syntax', file=sys.stderr)

        print_result(self.handler.program)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == '__main__':
    main()
