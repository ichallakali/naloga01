def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return a / b

if __name__ == "__main__":
    print("Mini Calc")
    op = input("Op (+,-,*,/): ").strip()
    a = float(input("a = "))
    b = float(input("b = "))
    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if op not in ops:
        print("Unknown op"); raise SystemExit(1)
    print(f"Result: {ops[op](a, b)}")
