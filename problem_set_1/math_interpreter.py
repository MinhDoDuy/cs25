# 4 Math Interpreter
express = input("Expression: ")
x, operator, y = express.strip()

x = float(x)
y = float(y)

if operator == '+':
    print(x + y)
elif operator == '-':
    print(x - y)
elif operator == '*':
    print(x * y)
elif operator == '/':
    print(x / y)
else:
    print("Wrong")