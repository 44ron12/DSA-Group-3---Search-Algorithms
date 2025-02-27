class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.is_empty():
            popped = self.top.data
            self.top = self.top.next
            return popped
        else:
            raise IndexError("Pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.top.data
        else:
            raise IndexError("Peek from an empty stack")

def stack_traverse(top):
    result = []
    current = top
    while current:
        result.append(current)
        current = current.next
    return result

def infix_to_postfix(infix):
    operator_precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    stack = Stack()

    print("Step\t|\tSymbol\t|\tStack\t|\tOutput")

    for step, char in enumerate(infix):
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()  # Discard '('
        else:
            while not stack.is_empty() and operator_precedence.get(char, 0) <= operator_precedence.get(stack.peek(), 0):
                output.append(stack.pop())
            stack.push(char)

        print(f"{step + 1}\t|\t{char}\t|\t{''.join([item.data for item in stack_traverse(stack.top)]) if stack.top else 'Empty'}\t|\t{''.join(output)}")

    # Use a separate variable for the second loop
    step_second_loop = step + 1

    while not stack.is_empty():
        output.append(stack.pop())
        print(f"{step_second_loop}\t|\t-\t|\t{''.join([item.data for item in stack_traverse(stack.top)]) if stack.top else 'Empty'}\t|\t{''.join(output)}")

    # Modify the function to return the result instead of printing
    result = {
        "steps": [],
        "infix_expression": infix,
        "postfix_expression": "",
    }

    for step, char in enumerate(infix):
        result["steps"].append({
            "step": step + 1,
            "symbol": char,
            "stack": ''.join([item.data for item in stack_traverse(stack.top)]) if stack.top else 'Empty',
            "output": ''.join(output),
        })

    while not stack.is_empty():
        output.append(stack.pop())
        result["steps"].append({
            "step": step_second_loop,
            "symbol": "-",
            "stack": ''.join([item.data for item in stack_traverse(stack.top)]) if stack.top else 'Empty',
            "output": ''.join(output),
        })

    result["postfix_expression"] = ''.join(output)

    return result
