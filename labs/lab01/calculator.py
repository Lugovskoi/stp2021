operation = input("Operation: ")
a = float(input("a:"))
b = float(input("b:"))

if operation == "+":
    c = a + b
elif operation == "-":
    c = a - b
print(str(a) + " " + operation + " " + str(b) + " = " + str(c))