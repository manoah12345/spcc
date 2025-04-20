# Intermediate Code Generation using 3 Address Code

class Conversion: 
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.array = []
        self.output = []
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
     
    def isEmpty(self):
        return self.top == -1
     
    def peek(self):
        return self.array[-1]
     
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"
    
    def push(self, op):
        self.top += 1
        self.array.append(op)
 
    def isOperand(self, ch):
        return ch.isalpha() or ch.isdigit()
 
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return a <= b
        except KeyError: 
            return False
             
    def infixToPostfix(self, exp):
        for i in exp:
            if self.isOperand(i):
                self.output.append(i)
            elif i == '(':
                self.push(i)
            elif i == ')':
                while not self.isEmpty() and self.peek() != '(':
                    self.output.append(self.pop())
                if not self.isEmpty() and self.peek() == '(':
                    self.pop()
            else:
                while not self.isEmpty() and self.notGreater(i):
                    self.output.append(self.pop())
                self.push(i)
        while not self.isEmpty():
            self.output.append(self.pop())
        print("\nPostfix notation: ", end="")
        print("".join(self.output))
        return "".join(self.output)

def T_A_C(exp):
    stack = []
    temp_count = 1
    obj = Conversion(len(exp))
    postfix = obj.infixToPostfix(exp)
    
    print("\nThree Address Code:")
    for i in postfix:
        if i.isalnum():
            stack.append(i)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            print(f"t{temp_count} = {op1} {i} {op2}")
            stack.append(f"t{temp_count}")
            temp_count += 1

def Quadruple(exp):
    stack = []
    temp_count = 1
    obj = Conversion(len(exp))
    postfix = obj.infixToPostfix(exp)
    
    print("\nQuadruple Representation:")
    print("{:^6} | {:^6} | {:^6} | {:^6}".format('op', 'arg1', 'arg2', 'result'))
    print("-" * 29)
    
    for i in postfix:
        if i.isalnum():
            stack.append(i)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            print("{:^6} | {:^6} | {:^6} | {:^6}".format(i, op1, op2, f"t{temp_count}"))
            stack.append(f"t{temp_count}")
            temp_count += 1

def Triple(exp):
    stack = []
    index = 0
    obj = Conversion(len(exp))
    postfix = obj.infixToPostfix(exp)
    
    print("\nTriple Representation:")
    print("{:^6} | {:^6} | {:^6} | {:^6}".format('#', 'op', 'arg1', 'arg2'))
    print("-" * 29)
    
    for i in postfix:
        if i.isalnum():
            stack.append(i)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            arg1 = op1 if isinstance(op1, str) and not op1.startswith('(') else f"({op1})"
            arg2 = op2 if isinstance(op2, str) and not op2.startswith('(') else f"({op2})"
            print("{:^6} | {:^6} | {:^6} | {:^6}".format(index, i, arg1, arg2))
            stack.append(index)
            index += 1

if __name__ == '__main__':
    print("Intermediate Code Generation using 3 Address Code")
    exp = input("Enter a valid infix expression: ").replace(" ", "")
    
    T_A_C(exp)
    Quadruple(exp)
    Triple(exp)
